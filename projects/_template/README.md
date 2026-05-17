# [Project Name] — 论文项目

> ⚠️ Agent 第一步读 [`WORKFLOW.md`](WORKFLOW.md) — 操作手册 + 三种会话模式 + 红线。

## 项目元数据

```yaml
title: [Tentative title]
target_venue: [NeurIPS / ICML / ICLR / CVPR / ACL / ...]
target_year: [2026]
deadline: [YYYY-MM-DD HH:MM TZ]
phase: [idea | experimenting | drafting | under-review | rebuttal | revising]
core_claim: [一句话 — 这篇 paper 主要 claim]
core_baselines: [Name1 (citekey1), Name2 (citekey2)]
core_datasets: [D1, D2, D3]
collaborators: [Name1, Name2]
```

## 当前 TODO

(由 agent 在 `/morning` 时帮忙更新；用户随时手动改)

- [ ] ...

## 目录速查

| 路径 | 用途 |
|------|------|
| `WORKFLOW.md` | **agent 操作手册** — 先读这个 |
| `draft/` | LaTeX 草稿（按章节拆分） |
| `figures/` | 论文图（脚本 + PDF + 共享 `matplotlib_settings.py`） |
| `data/` | 结果 CSV + `run_log.md` 实验日志 |
| `refs/` | BibTeX 主文件 |
| `response/` | Rebuttal tracker + 各轮 response 草稿 |
| `scripts/` | 一键复现 / rebuild 图脚本 |

## 进度日志

记录关键决定、卡点、灵感。Agent 在 `/morning` 末尾追加。

### YYYY-MM-DD
- 完成 / 决定 / 卡点

## Agent 偏好

- 章节模板用 `knowledge/templates/`
- 绘图风格用 `figures/matplotlib_settings.py` + `knowledge/methods/figure-standards.md`
- 投稿格式按 `knowledge/venues/<target>.md`
- 引用前检查 `refs/main.bib` 是否已收录，没有就标 `[CITE: 描述]`
- 实验数字必须能溯源到 `data/results.csv` 某行
