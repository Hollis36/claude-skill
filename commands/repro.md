# /repro — 复现性检查

调用 `skills/reproducible-research/` + `knowledge/methods/reproducibility-checklist.md`。

## 用法场景

- 投稿前最后检查
- Code release 前自查
- 复现别人 paper 时定位 gap

## 流程

### 投稿前（NeurIPS / ICML Checklist 对照）

逐条对照 `knowledge/methods/reproducibility-checklist.md`，对每条回答 Yes / No / N/A：

- [ ] 数据集：name + version + URL + license
- [ ] Train/val/test 划分
- [ ] 完整超参 + 选择方式
- [ ] 训练硬件 + 时长
- [ ] 随机种子数 ≥ 3 + std
- [ ] 统计显著性
- [ ] 计算资源量化
- [ ] 代码 + 模型权重 release 计划
- [ ] Limitations + Broader Impact
- [ ] LLM 使用声明

### Code release 自查

- [ ] README.md：5 行命令能复现主结果
- [ ] requirements.txt 精确 pin
- [ ] Dockerfile（强烈推荐）
- [ ] 一键脚本 `scripts/reproduce_table_X.sh`
- [ ] License 文件
- [ ] 删除 PII / 私有数据
- [ ] 在全新机器从 `git clone` 起跑通

### 复现别人 paper

1. 阅读 README + 论文 Appendix
2. 列出**论文 vs 代码不一致**的地方
3. 用论文报的 hyper（不是代码 default）
4. 验证主表数字（小数点 1 位匹配即可）
5. 若不能复现 → 通过 Issue 联系作者

## 推荐工具

- **Docker** — 完全隔离
- **Poetry / pip-tools** — 锁定依赖
- **DVC** — 数据版本控制
- **wandb / mlflow** — 实验追踪
- **anonymous.4open.science** — 评审期间匿名 repo

$ARGUMENTS
