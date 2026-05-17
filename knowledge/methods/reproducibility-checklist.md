# 复现性 Checklist（NeurIPS / ICML 对照）

NeurIPS 自 2019、ICML 自 2020 起强制要求 Reproducibility Checklist。这是**写完论文前最后一道关卡**。
完整流程见 `skills/reproducible-research/`。

## 论文里必须出现的（NeurIPS / ICML 通用）

### 算法 / 方法
- [ ] 完整描述算法步骤（**伪代码**优先于纯文字）
- [ ] 所有引入的概念都有**形式化定义**
- [ ] 关键 claim 有**理论证明**或**实验证据**
- [ ] 所有 assumption 明确列出
- [ ] **复杂度分析**（时间 / 空间）

### 实验设置
- [ ] **数据集**：名字、版本、来源 URL / DOI、是否公开
- [ ] **预处理**：完整步骤（normalization、tokenization、augmentation）
- [ ] **划分**：train / val / test 比例和方式（随机？固定 seed？跨 user？）
- [ ] **超参**：完整列表，包括如何选（grid search range、最终值）
- [ ] **训练**：epochs、batch size、optimizer、lr schedule、early stopping
- [ ] **硬件**：GPU 型号、数量、内存
- [ ] **运行时长**：单次训练耗时、总计算量
- [ ] **代码 / 模型权重 URL**（匿名版本用 anonymous.4open.science）

### 结果
- [ ] **随机种子数** ≥ 3，最好 ≥ 5
- [ ] **报告方差**（std / SEM / CI）
- [ ] **统计显著性**检验（见 `statistical-testing-ml.md`）
- [ ] **完整结果表格**（不要 cherry-pick）
- [ ] **失败案例 / 局限**讨论

### 数据
- [ ] 数据**来源、license、版本号**
- [ ] **人类标注**（若有）：标注流程、补偿、IRB
- [ ] **数据 sheet**（datasheet for datasets）— 大数据集必备
- [ ] **PII / 隐私**处理说明

## 代码提交清单

```
project/
├── README.md              ← 如何复现，命令复制即用
├── requirements.txt       ← 精确 pin 版本（pip freeze 或 poetry.lock）
├── environment.yml        ← conda env，含 Python 版本
├── Dockerfile             ← 最稳妥的复现保证
├── data/
│   └── README.md          ← 下载脚本或说明
├── configs/               ← 所有实验配置文件
├── src/                   ← 主代码
├── scripts/
│   ├── train.sh           ← 一键复现主结果
│   ├── eval.sh
│   └── reproduce_table_X.sh
├── notebooks/             ← 分析、画图
└── LICENSE
```

**README.md 必须有**：
1. 一段话项目描述
2. 安装步骤（5 行以内能跑通）
3. 数据下载命令
4. 复现主表的命令：`bash scripts/reproduce_table_1.sh`
5. 引用 BibTeX

## NeurIPS Reproducibility Checklist（论文末尾必填）

提交前对每条逐条回答 Yes / No / N/A，**说不的要解释**。完整列表：
https://neurips.cc/Conferences/2024/PaperInformation/PaperChecklist

核心问题（节选）：
1. Claims 准确性？
2. Limitations 讨论？
3. 理论结果完整 assumption + proof？
4. 信息足以复现主实验结果？
5. 是否开源 data + code？若否，是否提供详细 instructions？
6. 训练 / 测试细节完整？
7. error bar 报告？
8. 计算资源量化？
9. NeurIPS Code of Ethics 遵守？

## ICML / ICLR 差异

- **ICML**：类似 checklist，强调可复现实验
- **ICLR**：OpenReview 公开 review，复现性差易被攻击
- **CVPR**：相对宽松但近年趋严
- **ACL Rolling Review (ARR)**：Responsible NLP Research Checklist

## 提交前最后 24 小时

- [ ] 在一台**全新机器**（或 Docker 容器）从 git clone 起跑通
- [ ] 主表所有数字能从代码精确重现（小数点后 1 位）
- [ ] 代码仓库**匿名化**（去掉 author、commit history 中的邮箱）
- [ ] 数据 license 兼容 release
- [ ] Checklist 全部回答完
