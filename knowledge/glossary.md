# CS / AI 术语中英对照

写论文时统一术语；agent 翻译 / 起草时按此表。

## 机器学习基础

| 中文 | 英文 | 备注 |
|------|------|------|
| 监督学习 | supervised learning | |
| 无监督学习 | unsupervised learning | |
| 自监督学习 | self-supervised learning | |
| 半监督学习 | semi-supervised learning | |
| 强化学习 | reinforcement learning (RL) | |
| 迁移学习 | transfer learning | |
| 元学习 | meta-learning | |
| 联邦学习 | federated learning | |
| 因果推断 | causal inference | |
| 在线学习 | online learning | |
| 主动学习 | active learning | |
| 持续学习 | continual learning / lifelong learning | 避免用 incremental learning（含义略窄） |
| 多任务学习 | multi-task learning | |
| 课程学习 | curriculum learning | |
| 对比学习 | contrastive learning | |
| 自适应 | adaptive | 不要写 self-adaptive |

## 模型 / 架构

| 中文 | 英文 |
|------|------|
| 卷积神经网络 | convolutional neural network (CNN) |
| 循环神经网络 | recurrent neural network (RNN) |
| 长短期记忆 | long short-term memory (LSTM) |
| 门控循环单元 | gated recurrent unit (GRU) |
| 注意力机制 | attention mechanism |
| 自注意力 | self-attention |
| 多头注意力 | multi-head attention |
| Transformer | Transformer (大写 T) |
| 编码器-解码器 | encoder-decoder |
| 图神经网络 | graph neural network (GNN) |
| 大语言模型 | large language model (LLM) |
| 视觉语言模型 | vision-language model (VLM) |
| 扩散模型 | diffusion model |
| 生成对抗网络 | generative adversarial network (GAN) |
| 变分自编码器 | variational autoencoder (VAE) |
| 残差连接 | residual connection / skip connection |
| 归一化 | normalization (batch / layer / group) |

## 训练 / 优化

| 中文 | 英文 |
|------|------|
| 损失函数 | loss function |
| 目标函数 | objective function |
| 反向传播 | backpropagation |
| 梯度下降 | gradient descent |
| 学习率 | learning rate (lr) |
| 学习率调度 | learning rate schedule |
| 学习率预热 | warmup |
| 权重衰减 | weight decay |
| 批量大小 | batch size |
| 训练步 | training step / iteration |
| 训练轮 | epoch |
| 早停 | early stopping |
| 微调 | fine-tuning |
| 预训练 | pre-training |
| 提示工程 | prompt engineering |
| 上下文学习 | in-context learning (ICL) |
| 指令微调 | instruction tuning |
| 人类反馈强化学习 | reinforcement learning from human feedback (RLHF) |
| 直接偏好优化 | direct preference optimization (DPO) |
| 低秩适配 | low-rank adaptation (LoRA) |
| 知识蒸馏 | knowledge distillation |
| 量化 | quantization |
| 剪枝 | pruning |

## 评估 / 实验

| 中文 | 英文 |
|------|------|
| 训练集 | training set |
| 验证集 | validation set / dev set |
| 测试集 | test set |
| 留出 | held-out |
| 交叉验证 | cross-validation |
| 消融实验 | ablation study |
| 基线 | baseline |
| 准确率 | accuracy |
| 精确率 | precision |
| 召回率 | recall |
| 显著性检验 | significance test |
| 置信区间 | confidence interval |
| 效应量 | effect size |
| 误差 / 偏差 / 方差 | error / bias / variance |
| 过拟合 | overfitting |
| 欠拟合 | underfitting |
| 泛化 | generalization |
| 分布外 | out-of-distribution (OOD) |
| 同分布 | in-distribution (ID) |
| 鲁棒性 | robustness |
| 校准 | calibration |

## NLP 专用

| 中文 | 英文 |
|------|------|
| 分词 | tokenization |
| 词嵌入 | word embedding |
| 词表 | vocabulary |
| 命名实体识别 | named entity recognition (NER) |
| 关系抽取 | relation extraction |
| 共指消解 | coreference resolution |
| 机器翻译 | machine translation (MT) |
| 文本摘要 | text summarization (extractive / abstractive) |
| 问答 | question answering (QA) |
| 阅读理解 | reading comprehension |
| 对话系统 | dialogue system |
| 句法分析 | syntactic parsing |
| 依存分析 | dependency parsing |
| 语言模型 | language model |
| 困惑度 | perplexity |
| 幻觉 | hallucination |
| 检索增强生成 | retrieval-augmented generation (RAG) |

## CV 专用

| 中文 | 英文 |
|------|------|
| 图像分类 | image classification |
| 目标检测 | object detection |
| 语义分割 | semantic segmentation |
| 实例分割 | instance segmentation |
| 全景分割 | panoptic segmentation |
| 关键点检测 | keypoint detection |
| 姿态估计 | pose estimation |
| 边界框 | bounding box |
| 锚框 | anchor box |
| 数据增强 | data augmentation |
| 特征金字塔 | feature pyramid |
| 感受野 | receptive field |
| 视频理解 | video understanding |
| 神经辐射场 | neural radiance field (NeRF) |
| 三维重建 | 3D reconstruction |

## 写作易混

| 中文 | 推荐英文 | 不推荐 |
|------|---------|--------|
| 数据 | data (单复数同形，作复数动词) | datas, "the datas are" |
| 训练 | train (动) / training (名) | "do training" 弱 |
| 实验 | experiments (一般用复数) | "an experiment shows" 单数偶用 |
| 表示 | denote / represent | "show" 太弱 |
| 显著提升 | significant improvement | "huge"、"dramatic" 慎用 |
| 取得 SOTA | achieve state-of-the-art (SOTA) | "reach SOTA" |
| 我们提出 | we propose | "we suggest"（弱） |
| 我们发现 | we find / we observe | "we discover"（戏剧化） |
| 旨在 | aims to / is designed to | "wanna" 不行 |
| 综上所述 | in summary / overall | "all in all"（口语） |
| 此外 | furthermore / moreover / in addition | "besides"（口语） |
| 然而 | however / yet / nevertheless | "but"（口语，正文少用） |

## 易错拼写

- **state-of-the-art**（连字符）vs state of the art（不推荐）
- **dataset**（一词）vs data set（旧用法）
- **end-to-end**（连字符）
- **pre-training** vs pretraining — 两者都可，全文统一
- **fine-tuning** vs finetuning — 连字符更标准
- **zero-shot / few-shot / one-shot**（连字符）
- **multi-modal** vs multimodal — 两者都见，统一即可
- **trade-off**（连字符）vs tradeoff

## Hollis 偏好（可补充）

- 用 **method** 多于 **approach** / **technique**
- 用 **achieve** 多于 **reach** / **attain**
- 用 **demonstrate** 多于 **show**（在 contribution 列表里）
- 避免 **utilize** — 用 **use**
- 避免 **delve into** — ChatGPT 味太重
