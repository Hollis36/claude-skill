# Data

## 此目录存什么

- **实验结果摘要**：CSV / JSON 格式的汇总（每行一个 run）
- **绘图源数据**：与 `../figures/*.py` 配对的输入

## 此目录**不**存

- **原始数据集**（ImageNet / 自采数据） — 太大，放外部存储
- **训练好的模型权重** — 同上
- **wandb / tensorboard logs** — 同上
- **PII / 隐私数据** — 永远不进 git

## 命名约定

```
results_<experiment>_<date>.csv
```

例如 `results_main_table_2025-05-17.csv`。

## 推荐 CSV schema

```
seed, dataset, method, metric_name, metric_value, std, n_samples, notes
```

便于 pandas 读 + 后续绘图 + agent 解析。
