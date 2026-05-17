# References 文献笔记

## 用法

每篇有价值的文献复制 `_template.md`，命名为 `firstauthor-year-keyword.md`。
例如：`vaswani-2017-attention.md`。

## 为什么这样存

- **结构化** → agent 能解析、可写入 BibTeX
- **带评价** → 远超 Zotero 的纯收藏，体现你的判断
- **可检索** → 用 tag 系统按主题、年份、状态找

## 维护策略

- **新文献先存 BibTeX**（即使不读完），避免引用时找不到
- **读完写 TL;DR**（1 句话）
- **决定引用时**才写完整笔记
- **被引用过的文献** 加 `#status-cited` tag，方便追溯

## 与 Zotero / Notion 的关系

如果你已经在 Zotero / Notion 维护文献库：
- 这里**只存**与具体论文项目强相关的、需要给 agent 上下文的文献
- 不要试图 mirror 整个 Zotero — 维护成本太高
- 用 BibTeX export 的 `.bib` 放在具体项目下（`projects/<name>/refs/main.bib`）

## 推荐 agent 检索方式

```
Hollis 问"X 这篇怎么样" → agent 查 references/firstauthor-year-*.md
Hollis 问"这个方向最新进展" → agent 看 tags 找最近 #year-2024 / #year-2025
Hollis 写 paper 要引用 → agent 查 #status-cited，复制 BibTeX
```
