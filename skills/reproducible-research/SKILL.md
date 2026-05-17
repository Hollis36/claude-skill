---
name: reproducible-research
description: |
  可重复性研究助手，帮助科研人员构建可重复的计算工作流。支持Jupyter notebooks最佳实践、Docker/Singularity容器化、工作流管理(Snakemake/Nextflow)、代码和数据版本控制、环境管理(conda/venv)。当用户需要：(1) 确保研究的可重复性、(2) 创建可复现的分析流程、(3) 容器化计算环境、(4) 版本控制代码和数据时触发。关键词：可重复性、reproducibility、Jupyter、Docker、容器化、workflow、Snakemake。
license: Apache-2.0
---

# 可重复性研究助手

帮助科研人员构建可重复、可复现的计算研究工作流，确保研究结果的可验证性和可信度。

## 核心原则

### 可重复性研究的三个支柱
1. **代码版本控制**：使用Git追踪所有分析代码的变更
2. **环境管理**：明确记录计算环境（软件版本、依赖项）
3. **工作流自动化**：自动化数据处理和分析流程

## 1. Jupyter Notebooks 最佳实践

### 基本原则

```python
# Jupyter Notebook 最佳实践模板

# Cell 1: 文档说明
"""
# 数据分析: [项目名称]

**作者**: [姓名]
**日期**: 2026-04-06
**目的**: [简要描述分析目的]

## 环境要求
- Python 3.11
- pandas 2.0.0
- numpy 1.24.0
- matplotlib 3.7.0
"""

# Cell 2: 导入库（按类别组织）
# 标准库
import os
import sys
from pathlib import Path

# 第三方库 - 数据处理
import numpy as np
import pandas as pd

# 第三方库 - 可视化
import matplotlib.pyplot as plt
import seaborn as sns

# 第三方库 - 统计分析
from scipy import stats

# 设置
%matplotlib inline
%load_ext autoreload
%autoreload 2

# 可视化配置
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# 显示设置
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)

# Cell 3: 设置随机种子（确保可重复性）
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Cell 4: 定义路径
PROJECT_ROOT = Path.cwd().parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"
FIGURES_DIR = RESULTS_DIR / "figures"

# 创建目录
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Cell 5: 定义函数（将复杂逻辑封装为函数）
def load_data(file_path):
    """加载数据文件

    Args:
        file_path: 数据文件路径

    Returns:
        DataFrame: 加载的数据
    """
    df = pd.read_csv(file_path)
    print(f"加载数据: {df.shape[0]} 行, {df.shape[1]} 列")
    return df

def preprocess_data(df):
    """数据预处理

    Args:
        df: 原始数据

    Returns:
        DataFrame: 处理后的数据
    """
    # 处理缺失值
    df = df.dropna()

    # 数据转换
    # ...

    return df

# Cell 6+: 分析步骤（每个cell一个逻辑步骤）
# 每个分析步骤包含：
# 1. Markdown说明
# 2. 代码实现
# 3. 结果展示
```

### Jupyter配置文件（推荐设置）

```python
# jupyter_notebook_config.py
# 生成配置: jupyter notebook --generate-config

c = get_config()

# 自动保存间隔（毫秒）
c.FileContentsManager.autosave_interval = 60000  # 1分钟

# 关闭令牌认证（仅本地使用）
# c.NotebookApp.token = ''
# c.NotebookApp.password = ''

# 启动时不打开浏览器
c.NotebookApp.open_browser = False

# 允许远程访问（谨慎使用）
# c.NotebookApp.ip = '0.0.0.0'
```

### Notebook转换和版本控制

```bash
# 将notebook转换为Python脚本（便于版本控制）
jupyter nbconvert --to script analysis.ipynb

# 清理notebook输出（减小文件大小）
jupyter nbconvert --clear-output --inplace analysis.ipynb

# 使用nbdime进行notebook diff和merge
pip install nbdime
nbdime config-git --enable --global

# Git配置 .gitattributes
echo "*.ipynb filter=nbstripout" >> .gitattributes
pip install nbstripout
nbstripout --install --attributes .gitattributes
```

### Papermill: 参数化Notebook

```python
# 安装
pip install papermill

# 将notebook参数化
# 在notebook中添加参数cell，标记为 "parameters"
"""
# Parameters cell (标记为 parameters)
input_file = "data.csv"
output_dir = "results"
threshold = 0.05
"""

# 使用papermill执行notebook
import papermill as pm

pm.execute_notebook(
    'analysis_template.ipynb',
    'analysis_output.ipynb',
    parameters=dict(
        input_file='experiment_001.csv',
        output_dir='results/exp001',
        threshold=0.01
    )
)
```

## 2. 环境管理

### Conda环境管理

```bash
# 创建新环境
conda create -n myproject python=3.11

# 激活环境
conda activate myproject

# 安装包
conda install numpy pandas matplotlib scipy jupyter

# 导出环境（精确版本）
conda env export > environment.yml

# 从environment.yml创建环境
conda env create -f environment.yml

# 更新环境
conda env update -f environment.yml --prune
```

### environment.yml示例

```yaml
name: myproject
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy=1.24.0
  - pandas=2.0.0
  - matplotlib=3.7.0
  - scipy=1.10.0
  - jupyter=1.0.0
  - pip=23.0.0
  - pip:
    - scikit-learn==1.2.2
    - seaborn==0.12.2
```

### Python虚拟环境（venv）

```bash
# 创建虚拟环境
python -m venv venv

# 激活（Linux/Mac）
source venv/bin/activate

# 激活（Windows）
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 生成requirements.txt（精确版本）
pip freeze > requirements.txt

# 生成requirements.txt（推荐格式）
pip install pipreqs
pipreqs . --force
```

### requirements.txt示例

```
numpy==1.24.0
pandas==2.0.0
matplotlib==3.7.0
scipy==1.10.0
scikit-learn==1.2.2
seaborn==0.12.2
jupyter==1.0.0
```

### Poetry: 现代Python依赖管理

```bash
# 安装Poetry
curl -sSL https://install.python-poetry.org | python3 -

# 初始化项目
poetry init

# 添加依赖
poetry add numpy pandas matplotlib

# 添加开发依赖
poetry add --group dev pytest black flake8

# 安装依赖
poetry install

# 运行命令
poetry run python script.py
poetry run jupyter lab
```

### pyproject.toml示例

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "Research project"
authors = ["Your Name <your.email@example.com>"]

[tool.poetry.dependencies]
python = "^3.11"
numpy = "^1.24.0"
pandas = "^2.0.0"
matplotlib = "^3.7.0"
scipy = "^1.10.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.3.0"
black = "^23.3.0"
flake8 = "^6.0.0"
jupyter = "^1.0.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

## 3. Docker容器化

### 基础Dockerfile示例

```dockerfile
# Dockerfile for Python scientific computing
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装Python依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 默认命令
CMD ["python", "main.py"]
```

### Jupyter Lab Docker

```dockerfile
# Dockerfile for Jupyter Lab
FROM jupyter/scipy-notebook:latest

USER root

# 安装额外依赖
RUN apt-get update && apt-get install -y \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

USER $NB_UID

# 安装Python包
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 设置工作目录
WORKDIR /home/jovyan/work

# 暴露端口
EXPOSE 8888

# 启动Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]
```

### docker-compose.yml

```yaml
version: '3.8'

services:
  jupyter:
    build: .
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
      - ./data:/home/jovyan/data
    environment:
      - JUPYTER_ENABLE_LAB=yes
    command: jupyter lab --ip=0.0.0.0 --allow-root --NotebookApp.token=''

  analysis:
    build: .
    volumes:
      - ./code:/app/code
      - ./data:/app/data
      - ./results:/app/results
    command: python code/analysis.py
```

### 使用Docker

```bash
# 构建镜像
docker build -t myproject:latest .

# 运行容器
docker run -it --rm \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/results:/app/results \
  myproject:latest

# 使用docker-compose
docker-compose up -d
docker-compose logs -f
docker-compose down

# 进入运行中的容器
docker exec -it <container_id> /bin/bash
```

## 4. Singularity容器（HPC环境）

### Singularity Definition File

```singularity
Bootstrap: docker
From: python:3.11-slim

%post
    # 安装系统依赖
    apt-get update
    apt-get install -y build-essential git

    # 安装Python依赖
    pip install numpy pandas matplotlib scipy scikit-learn

%environment
    export LC_ALL=C
    export PATH=/usr/local/bin:$PATH

%runscript
    exec python "$@"

%labels
    Author your.email@example.com
    Version v0.1.0

%help
    This container provides a Python 3.11 environment for scientific computing.

    Usage:
    singularity run container.sif script.py
```

### 构建和使用Singularity

```bash
# 构建容器（需要root权限）
sudo singularity build myproject.sif myproject.def

# 运行容器
singularity run myproject.sif analysis.py

# 绑定挂载目录
singularity run --bind /data:/mnt/data myproject.sif

# 启动Shell
singularity shell myproject.sif

# 从Docker Hub构建
singularity build python.sif docker://python:3.11
```

## 5. 工作流管理

### Snakemake工作流

```python
# Snakefile
configfile: "config.yaml"

# 全部目标
rule all:
    input:
        "results/final_report.html"

# 数据预处理
rule preprocess:
    input:
        "data/raw/{sample}.csv"
    output:
        "data/processed/{sample}.csv"
    script:
        "scripts/preprocess.py"

# 数据分析
rule analyze:
    input:
        "data/processed/{sample}.csv"
    output:
        "results/{sample}_results.csv"
    params:
        threshold=config["threshold"]
    script:
        "scripts/analyze.py"

# 生成图表
rule plot:
    input:
        "results/{sample}_results.csv"
    output:
        "results/figures/{sample}_plot.png"
    script:
        "scripts/plot.py"

# 生成报告
rule report:
    input:
        expand("results/{sample}_results.csv", sample=config["samples"]),
        expand("results/figures/{sample}_plot.png", sample=config["samples"])
    output:
        "results/final_report.html"
    script:
        "scripts/generate_report.py"
```

### config.yaml

```yaml
# 配置文件
samples:
  - sample1
  - sample2
  - sample3

threshold: 0.05

output_format: "html"
```

### 运行Snakemake

```bash
# 安装
pip install snakemake

# 运行工作流
snakemake --cores 4

# 干运行（查看将执行的任务）
snakemake -n

# 生成工作流图
snakemake --dag | dot -Tpng > workflow.png

# 生成报告
snakemake --report report.html

# 使用conda环境
snakemake --use-conda --cores 4
```

### Nextflow工作流

```groovy
// main.nf
#!/usr/bin/env nextflow

params.input = 'data/raw/*.csv'
params.outdir = 'results'

// 数据预处理
process preprocess {
    input:
    path input_file

    output:
    path "${input_file.baseName}_processed.csv"

    script:
    """
    python scripts/preprocess.py $input_file ${input_file.baseName}_processed.csv
    """
}

// 数据分析
process analyze {
    publishDir "${params.outdir}", mode: 'copy'

    input:
    path processed_file

    output:
    path "${processed_file.baseName}_results.csv"

    script:
    """
    python scripts/analyze.py $processed_file ${processed_file.baseName}_results.csv
    """
}

// 工作流定义
workflow {
    input_ch = Channel.fromPath(params.input)
    preprocess(input_ch) | analyze
}
```

### 运行Nextflow

```bash
# 安装
curl -s https://get.nextflow.io | bash

# 运行工作流
nextflow run main.nf

# 恢复工作流
nextflow run main.nf -resume

# 使用Docker
nextflow run main.nf -with-docker myimage:latest

# 生成报告
nextflow run main.nf -with-report report.html -with-timeline timeline.html
```

## 6. 数据版本控制（DVC）

### 基础使用

```bash
# 安装
pip install dvc

# 初始化
dvc init

# 添加远程存储
dvc remote add -d storage s3://mybucket/dvcstore
# 或使用本地存储
dvc remote add -d storage /tmp/dvc-storage

# 追踪大文件
dvc add data/large_dataset.csv

# 提交到Git（只提交.dvc元数据文件）
git add data/large_dataset.csv.dvc data/.gitignore
git commit -m "Add large dataset"

# 推送数据到远程存储
dvc push

# 拉取数据
dvc pull

# 切换数据版本
git checkout v1.0
dvc checkout
```

### DVC Pipeline

```yaml
# dvc.yaml
stages:
  preprocess:
    cmd: python scripts/preprocess.py data/raw data/processed
    deps:
      - data/raw
      - scripts/preprocess.py
    outs:
      - data/processed

  train:
    cmd: python scripts/train.py data/processed models/
    deps:
      - data/processed
      - scripts/train.py
    outs:
      - models/model.pkl
    metrics:
      - metrics/train_metrics.json:
          cache: false

  evaluate:
    cmd: python scripts/evaluate.py models/model.pkl data/test
    deps:
      - models/model.pkl
      - data/test
      - scripts/evaluate.py
    metrics:
      - metrics/eval_metrics.json:
          cache: false
```

### 运行DVC Pipeline

```bash
# 运行pipeline
dvc repro

# 查看pipeline图
dvc dag

# 比较指标
dvc metrics show
dvc metrics diff HEAD~1

# 查看参数
dvc params show
dvc params diff
```

## 7. 完整项目结构示例

```
research-project/
├── README.md                 # 项目说明
├── LICENSE                   # 许可证
├── .gitignore               # Git忽略文件
├── .gitattributes           # Git属性
├── environment.yml          # Conda环境
├── requirements.txt         # Python依赖
├── Dockerfile               # Docker配置
├── docker-compose.yml       # Docker Compose配置
├── Snakefile               # Snakemake工作流
├── dvc.yaml                # DVC pipeline
├── data/                   # 数据目录（不提交到Git）
│   ├── raw/                # 原始数据
│   ├── processed/          # 处理后数据
│   └── .gitignore          # 忽略数据文件
├── notebooks/              # Jupyter notebooks
│   ├── 01_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   └── 03_analysis.ipynb
├── scripts/                # 脚本
│   ├── preprocess.py
│   ├── analyze.py
│   └── plot.py
├── src/                    # 源代码（可安装模块）
│   ├── __init__.py
│   ├── data.py
│   ├── models.py
│   └── utils.py
├── tests/                  # 测试
│   ├── test_data.py
│   └── test_models.py
├── results/                # 结果（不提交到Git）
│   ├── figures/
│   └── tables/
├── docs/                   # 文档
│   └── methods.md
└── config/                 # 配置文件
    └── config.yaml
```

### README.md模板

```markdown
# 项目名称

简要描述项目目的和主要发现。

## 环境设置

### 使用Conda
```bash
conda env create -f environment.yml
conda activate myproject
```

### 使用Docker
```bash
docker-compose up -d
```

## 数据

数据来源：[描述数据来源]
数据访问：[提供数据访问链接或说明]

原始数据存放在 `data/raw/`
处理后数据存放在 `data/processed/`

## 分析流程

1. 数据预处理：`notebooks/01_exploration.ipynb`
2. 数据分析：`notebooks/02_analysis.ipynb`
3. 结果可视化：`notebooks/03_visualization.ipynb`

或使用自动化工作流：
```bash
snakemake --cores 4
```

## 重现结果

```bash
# 克隆仓库
git clone https://github.com/username/project.git
cd project

# 设置环境
conda env create -f environment.yml
conda activate myproject

# 获取数据
dvc pull

# 运行分析
snakemake --cores 4

# 查看结果
ls results/
```

## 引用

如果使用本项目，请引用：
```
Author et al. (2026). Title. Journal, Volume(Issue), Pages.
```

## 许可证

Apache License 2.0
```

## 8. 可重复性检查清单

在发表或分享研究前，确保：

### 代码
- [ ] 所有分析代码已提交到版本控制
- [ ] 代码有清晰的注释和文档
- [ ] 随机种子已固定
- [ ] 代码可以在新环境中运行

### 环境
- [ ] 提供environment.yml或requirements.txt
- [ ] 记录Python/R版本
- [ ] 记录关键库的版本号
- [ ] 提供Docker/Singularity容器（可选但推荐）

### 数据
- [ ] 原始数据有备份
- [ ] 数据处理步骤有完整记录
- [ ] 数据访问方式已说明
- [ ] 数据使用符合伦理和隐私要求

### 工作流
- [ ] 分析步骤可自动化执行
- [ ] 工作流有清晰文档
- [ ] 中间结果可验证
- [ ] 最终结果可重现

### 文档
- [ ] README文件完整
- [ ] 提供重现步骤
- [ ] 列出已知问题和限制
- [ ] 提供联系方式

## 9. 常用工具总结

| 类别 | 工具 | 用途 |
|------|------|------|
| **Notebook** | Jupyter Lab | 交互式分析 |
| | Google Colab | 云端协作 |
| | Papermill | Notebook参数化 |
| **环境管理** | Conda | 跨语言环境管理 |
| | Poetry | Python依赖管理 |
| | renv | R环境管理 |
| **容器化** | Docker | 通用容器 |
| | Singularity | HPC容器 |
| **工作流** | Snakemake | Python工作流 |
| | Nextflow | 通用工作流 |
| | CWL | 标准化工作流 |
| **版本控制** | Git | 代码版本控制 |
| | DVC | 数据版本控制 |
| | Git LFS | 大文件存储 |

## 10. 参考资源

- [Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)
- [The Turing Way: Guide for Reproducible Research](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html)
- [Software Carpentry: Version Control with Git](https://swcarpentry.github.io/git-novice/)
- [Docker Documentation](https://docs.docker.com/)
- [Snakemake Documentation](https://snakemake.readthedocs.io/)
- [Jupyter Best Practices](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/examples_index.html)
