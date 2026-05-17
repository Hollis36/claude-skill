# examples/

完整填好的**示范 project**，给 agent 当 few-shot 参考、给用户当样本看。**不是真实论文**，数据全是合成。

## 当前 examples

| 路径 | 演示什么 |
|------|---------|
| `rebuttal-paper/` | NeurIPS rebuttal phase — 3 reviewer / 部分实验完成 / 部分 rebuttal 草稿写好 |

## 为什么放在这

- `projects/*` 默认 gitignore（保护真实论文隐私）
- 示范要进库让 agent 能读 → 放 `examples/`
- 名字明确"example"，不会和真实项目混淆

## 如何使用

1. **读者视角**：想看完整工作流跑起来啥样，直接读对应目录的 `README.md` + `WORKFLOW.md` + `response/rebuttal-tracker.md`
2. **Agent 视角**：作为参考"一个填好的项目长什么样"，可以问 agent "看看 `examples/rebuttal-paper/` 是怎么填的，我也照这个填"
3. **起新项目**：不要复制 `examples/`，复制 `projects/_template/`。`/init` 命令也用 _template
