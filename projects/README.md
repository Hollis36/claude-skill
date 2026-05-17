# Projects

具体论文项目目录。**不进入主仓库公开**部分 — 通过 `.gitignore` 管理或单独私有仓库。

## 起步

```bash
cp -r projects/_template projects/<paper-name>
# 编辑 projects/<paper-name>/README.md 填元数据
```

## 命名

用 short keyword + year，例如：
- `attention-routing-2025`
- `efficient-rag-2026`

避免用真实论文标题作目录名（万一被偷看）。

## 隐私

此目录默认 `.gitignore` 排除（见仓库根 `.gitignore`）。
如果某项目已公开（投稿后），可以在 `.gitignore` 里加 `!projects/<paper-name>/` 反转。

## Agent 用法

Hollis 说"在 X 项目里"时，agent 进 `projects/X/`，读 `README.md` 拿元数据，按 `draft/` `figures/` `data/` `refs/` `response/` 各司其职。
