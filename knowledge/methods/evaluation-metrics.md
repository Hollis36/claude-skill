# 评估指标速查（CS / AI）

## 分类

| 指标 | 何时用 | 何时**不**用 |
|------|--------|-------------|
| Accuracy | 类别平衡、错误成本对称 | 类别不平衡（用 F1 / AUROC） |
| Precision / Recall | 关心特定类、需要 trade-off | 两者必须一起报 |
| F1 (macro / micro / weighted) | 多分类、不平衡 | 区分清楚 macro vs micro，论文里说明 |
| AUROC | 二分类、阈值无关比较 | 极度不平衡（≪ 1% 正类，用 AUPRC） |
| AUPRC / AP | 不平衡、关心正类 | 推荐配合 AUROC 一起报 |
| Cohen's κ | 评估 vs 标注者一致性 | 单独评估模型，先用 F1 |
| MCC | 不平衡二分类的综合指标 | 多分类（用 macro-F1） |
| Calibration (ECE) | 关心概率可靠性 | 只关心 top-1 决策时次要 |

## 目标检测 / 分割

- **mAP@0.5 / mAP@0.5:0.95** — COCO 标准，必报
- **IoU** — 单 box / mask
- **Dice / Jaccard** — 医学影像分割
- **Panoptic Quality (PQ)** — 全景分割
- **HD95 / ASSD** — 医学分割边界

## 生成 / 图像

| 指标 | 说明 | 注意 |
|------|------|------|
| FID | Fréchet Inception Distance | 50k 样本起步，少了不可信；用相同 backbone 比 |
| IS | Inception Score | 已不推荐主指标 |
| CLIP Score | 文本-图像对齐 | 不同 CLIP 版本不可比 |
| LPIPS | 感知相似度 | 报告时注明 backbone (alex / vgg) |
| PSNR / SSIM | 像素级 / 结构相似 | 高质量生成易饱和 |
| Precision / Recall (Kynkäänniemi 2019) | 多样性 vs 真实性 | 配合 FID 更全面 |

## NLP / 生成

| 指标 | 何时用 |
|------|--------|
| BLEU-N | 机器翻译，N=4 标准；短文本慎用 |
| ROUGE-1/2/L | 摘要 |
| METEOR | 翻译，考虑同义词 |
| BERTScore | 语义相似，需固定模型版本 |
| Perplexity | 语言模型；只在同 tokenizer 下可比 |
| Exact Match / F1 | QA |
| Pass@k | 代码生成（HumanEval、MBPP） |
| Win rate (vs baseline) | 偏好评估，需说明评估者（人 / LLM judge） |

## LLM 评估

- **MMLU / MMLU-Pro** — 通用知识
- **BBH / AGIEval** — 推理
- **HumanEval / MBPP / SWE-bench** — 代码
- **HellaSwag / ARC / WinoGrande** — 常识
- **TruthfulQA** — 幻觉
- **MT-Bench / AlpacaEval / Chatbot Arena** — 对话偏好
- **Needle-in-Haystack / RULER** — 长上下文

**用 LLM 作评判者时**：固定 judge 模型版本、prompt、温度；报告与人类评价的相关性；考虑 position bias / verbosity bias。

## 必须同时报告的"配套数据"

- 不只报指标值，还要报：
  - **方差** — 至少 3 个 seed 的 mean ± std
  - **置信区间** — 95% CI（bootstrap）
  - **统计显著性** — 与基线对比的 p-value（见 `statistical-testing-ml.md`）
  - **计算成本** — 参数量 / FLOPs / 训练时长 / 显存
  - **使用的具体 split / version** — 数据集 v1 vs v2 不可比

## 报告原则

1. 选指标要**和现有 SOTA 论文一致**，便于横向比较
2. 不要只报对你有利的指标 — 全套指标都报，弱项放在 Appendix
3. 表格中**↑↓ 箭头标方向**，**粗体最优值**，**下划线次优值**
4. **数据集版本必须明确**（"ImageNet" 不够，要说 ILSVRC2012 train/val）
