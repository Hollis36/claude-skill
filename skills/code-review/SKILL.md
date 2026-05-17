---
name: code-review
description: |
  科研代码审查助手，专注于确保科研代码的正确性、可重复性和可维护性。支持代码质量检查、安全漏洞扫描、可重复性验证、数据完整性检查、最佳实践验证。当用户需要：(1) 审查科研代码质量、(2) 确保实验代码可重复、(3) 检查数据分析脚本、(4) 验证统计分析代码、(5) 准备代码发布或提交论文时触发。关键词：code review、代码审查、代码质量、peer review、科研代码。
license: Apache-2.0
---

# 科研代码审查助手

帮助科研人员系统化地审查代码，确保研究代码的质量、正确性和可重复性。

## 核心原则

### 科研代码审查的四个维度

1. **正确性** - 代码是否正确实现了研究方法
2. **可重复性** - 他人能否复现研究结果
3. **可维护性** - 代码是否清晰、有文档、易于理解
4. **数据完整性** - 数据处理是否安全、准确

## 审查流程

### 第一阶段：预审查准备

在开始代码审查前，收集必要信息：

```markdown
## 代码审查准备清单

### 基本信息
- [ ] 代码用途和研究目标
- [ ] 预期输入和输出
- [ ] 使用的数据集和数据格式
- [ ] 依赖的软件包和版本
- [ ] 已知的限制和假设

### 审查范围
- [ ] 需要审查的文件列表
- [ ] 关键函数和模块
- [ ] 测试覆盖情况
- [ ] 文档完整性

### 参考材料
- [ ] 相关论文和方法描述
- [ ] 现有测试和验证
- [ ] 以前的审查反馈
```

### 第二阶段：代码结构审查

#### 项目组织

```python
# 检查项目结构是否清晰
def check_project_structure():
    """
    理想的科研项目结构：

    project/
    ├── README.md              # 项目说明
    ├── requirements.txt       # 依赖列表
    ├── environment.yml        # Conda环境
    ├── data/                  # 数据目录
    │   ├── raw/              # 原始数据
    │   ├── processed/        # 处理后数据
    │   └── README.md         # 数据说明
    ├── src/                   # 源代码
    │   ├── __init__.py
    │   ├── preprocessing.py
    │   ├── analysis.py
    │   └── visualization.py
    ├── notebooks/             # Jupyter notebooks
    ├── tests/                 # 测试代码
    ├── scripts/               # 运行脚本
    ├── results/               # 结果输出
    └── docs/                  # 文档
    """
    pass
```

**审查要点：**
- [ ] 目录结构清晰合理
- [ ] README 文件完整
- [ ] 数据和代码分离
- [ ] 结果和代码分离
- [ ] 有适当的 .gitignore

#### 代码模块化

```python
# 反模式：所有代码在一个文件中
# ❌ BAD
def analysis():
    # 1000+ 行代码在一个函数中
    data = load_data()
    # ... 大量处理逻辑
    plot_results()

# 最佳实践：模块化和单一职责
# ✅ GOOD
from src.data import load_data, preprocess_data
from src.analysis import run_statistical_test
from src.visualization import plot_results

def main():
    """主分析流程"""
    # 步骤1: 加载数据
    raw_data = load_data('data/raw/experiment.csv')

    # 步骤2: 预处理
    clean_data = preprocess_data(raw_data)

    # 步骤3: 统计分析
    results = run_statistical_test(clean_data)

    # 步骤4: 可视化
    plot_results(results, output='results/figures/')

    return results
```

**审查要点：**
- [ ] 函数职责单一（每个函数做一件事）
- [ ] 函数长度合理（< 50 行）
- [ ] 避免重复代码（DRY原则）
- [ ] 适当的抽象层次

### 第三阶段：代码正确性审查

#### 数值计算正确性

```python
import numpy as np
import pandas as pd

# 常见错误：整数除法
# ❌ BAD (Python 2 style)
mean = sum(values) / len(values)  # 可能产生整数除法错误

# ✅ GOOD
mean = sum(values) / float(len(values))
# 或使用 numpy
mean = np.mean(values)

# 常见错误：浮点数比较
# ❌ BAD
if calculated_value == expected_value:
    print("Match!")

# ✅ GOOD
import math
if math.isclose(calculated_value, expected_value, rel_tol=1e-9):
    print("Match!")

# 常见错误：数组索引
# ❌ BAD - 可能索引错误
for i in range(len(data)):
    result[i] = process(data[i])

# ✅ GOOD - 使用enumerate
for i, value in enumerate(data):
    result[i] = process(value)

# 或更好的向量化操作
result = np.array([process(x) for x in data])
```

#### 统计分析正确性

```python
from scipy import stats

# 检查假设是否满足
def check_statistical_assumptions(data):
    """检查统计检验的假设"""
    issues = []

    # 1. 检查样本量
    if len(data) < 30:
        issues.append(f"样本量较小 (n={len(data)}), 考虑使用非参数检验")

    # 2. 检查正态性
    _, p_value = stats.shapiro(data)
    if p_value < 0.05:
        issues.append(f"数据不满足正态分布 (p={p_value:.4f})")

    # 3. 检查异常值
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    outliers = np.sum((data < Q1 - 1.5*IQR) | (data > Q3 + 1.5*IQR))
    if outliers > 0:
        issues.append(f"检测到 {outliers} 个异常值")

    return issues

# 使用示例
issues = check_statistical_assumptions(data)
if issues:
    print("警告：")
    for issue in issues:
        print(f"  - {issue}")
```

**审查要点：**
- [ ] 统计方法选择正确
- [ ] 假设检验已执行
- [ ] 多重比较已校正
- [ ] 效应量已计算
- [ ] 置信区间已报告

#### 数据处理正确性

```python
import pandas as pd

# 常见错误：链式赋值警告
# ❌ BAD
df[df['age'] > 30]['category'] = 'old'  # SettingWithCopyWarning

# ✅ GOOD
df.loc[df['age'] > 30, 'category'] = 'old'

# 常见错误：缺失值处理不当
# ❌ BAD - 静默删除
df = df.dropna()

# ✅ GOOD - 记录和报告
print(f"原始数据: {len(df)} 行")
missing_counts = df.isnull().sum()
print(f"缺失值统计:\n{missing_counts[missing_counts > 0]}")
df_clean = df.dropna()
print(f"删除缺失值后: {len(df_clean)} 行 ({len(df)-len(df_clean)} 行被删除)")

# 常见错误：未处理重复数据
# ❌ BAD - 未检查重复
data = pd.read_csv('data.csv')

# ✅ GOOD - 检查并处理重复
data = pd.read_csv('data.csv')
duplicates = data.duplicated().sum()
if duplicates > 0:
    print(f"警告: 发现 {duplicates} 个重复行")
    data = data.drop_duplicates()
```

**审查要点：**
- [ ] 缺失值处理策略明确
- [ ] 异常值检测和处理
- [ ] 数据类型正确
- [ ] 重复数据已处理
- [ ] 数据转换有记录

### 第四阶段：可重复性审查

#### 随机种子固定

```python
import numpy as np
import random
import tensorflow as tf

# ❌ BAD - 没有设置随机种子
model = train_model(data)

# ✅ GOOD - 固定所有随机种子
def set_random_seeds(seed=42):
    """设置所有随机数生成器的种子"""
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)
    # 如果使用PyTorch
    # import torch
    # torch.manual_seed(seed)
    # torch.cuda.manual_seed_all(seed)

    print(f"随机种子已设置为: {seed}")

# 在代码开始时调用
set_random_seeds(42)
model = train_model(data)
```

#### 依赖版本管理

```python
# requirements.txt (固定版本)
# ✅ GOOD
numpy==1.24.0
pandas==2.0.0
scipy==1.10.0
matplotlib==3.7.0
scikit-learn==1.2.2

# ❌ BAD (不固定版本)
numpy
pandas
scipy
```

```yaml
# environment.yml (Conda环境)
name: research-project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy=1.24.0
  - pandas=2.0.0
  - scipy=1.10.0
  - matplotlib=3.7.0
  - pip:
    - scikit-learn==1.2.2
```

**审查要点：**
- [ ] 随机种子已固定
- [ ] 依赖版本已锁定
- [ ] 环境可重建（environment.yml 或 requirements.txt）
- [ ] 数据来源可追溯
- [ ] 中间结果可保存

#### 路径处理

```python
import os
from pathlib import Path

# ❌ BAD - 硬编码绝对路径
data = pd.read_csv('/Users/username/project/data/data.csv')

# ❌ BAD - 依赖当前工作目录
data = pd.read_csv('data/data.csv')

# ✅ GOOD - 使用相对于脚本的路径
script_dir = Path(__file__).parent
data_file = script_dir / 'data' / 'data.csv'
data = pd.read_csv(data_file)

# ✅ BETTER - 使用项目根目录
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
data_file = DATA_DIR / 'raw' / 'data.csv'
data = pd.read_csv(data_file)
```

**审查要点：**
- [ ] 无硬编码路径
- [ ] 使用 Path 对象（跨平台）
- [ ] 路径相对于项目根目录
- [ ] 配置文件管理路径

### 第五阶段：代码质量审查

#### 命名规范

```python
# ❌ BAD - 无意义的名称
def f(x, y):
    z = x + y
    return z

# ✅ GOOD - 描述性名称
def calculate_total_score(baseline_score, bonus_points):
    """计算总分（基准分 + 奖励分）"""
    total_score = baseline_score + bonus_points
    return total_score

# ❌ BAD - 缩写不清晰
df = pd.read_csv('data.csv')
for i in range(len(df)):
    val = df.iloc[i]['col']

# ✅ GOOD - 清晰的命名
experiment_data = pd.read_csv('data.csv')
for index, row in experiment_data.iterrows():
    measurement_value = row['measurement']
```

**命名规范：**
- 变量：小写下划线 `variable_name`
- 函数：小写下划线 `function_name`
- 类：驼峰命名 `ClassName`
- 常量：大写下划线 `CONSTANT_NAME`

#### 文档字符串

```python
# ❌ BAD - 无文档
def calculate_statistics(data):
    return np.mean(data), np.std(data)

# ✅ GOOD - 完整的文档字符串
def calculate_statistics(data):
    """计算描述性统计量

    Args:
        data (array-like): 数值型数据数组

    Returns:
        tuple: (均值, 标准差)

    Raises:
        ValueError: 如果数据为空或包含非数值

    Example:
        >>> data = [1, 2, 3, 4, 5]
        >>> mean, std = calculate_statistics(data)
        >>> print(f"Mean: {mean:.2f}, Std: {std:.2f}")
        Mean: 3.00, Std: 1.41
    """
    if len(data) == 0:
        raise ValueError("数据不能为空")

    mean = np.mean(data)
    std = np.std(data, ddof=1)  # 样本标准差

    return mean, std
```

**审查要点：**
- [ ] 所有函数有文档字符串
- [ ] 参数类型和含义清晰
- [ ] 返回值说明
- [ ] 异常情况说明
- [ ] 包含使用示例

#### 代码注释

```python
# ❌ BAD - 无用的注释
x = x + 1  # 将x加1

# ❌ BAD - 注释代码而不是删除
# old_method(data)
new_method(data)

# ✅ GOOD - 解释为什么这样做
# 使用Welch's t-test因为两组方差不齐（Levene检验 p < 0.05）
t_stat, p_value = stats.ttest_ind(group1, group2, equal_var=False)

# ✅ GOOD - 解释复杂算法
# Smith-Waterman算法：
# 1. 初始化得分矩阵
# 2. 填充矩阵（动态规划）
# 3. 回溯找到最优对齐
alignment = smith_waterman(seq1, seq2)
```

**审查要点：**
- [ ] 注释解释"为什么"而不是"是什么"
- [ ] 复杂算法有说明
- [ ] 无注释掉的代码
- [ ] 关键决策有记录

### 第六阶段：测试和验证审查

#### 单元测试

```python
import pytest
import numpy as np
from src.analysis import calculate_statistics

def test_calculate_statistics_basic():
    """测试基本统计计算"""
    data = [1, 2, 3, 4, 5]
    mean, std = calculate_statistics(data)

    assert np.isclose(mean, 3.0)
    assert np.isclose(std, 1.5811, rtol=1e-4)

def test_calculate_statistics_empty():
    """测试空数据异常处理"""
    with pytest.raises(ValueError, match="数据不能为空"):
        calculate_statistics([])

def test_calculate_statistics_single_value():
    """测试单个值的情况"""
    data = [5.0]
    mean, std = calculate_statistics(data)

    assert mean == 5.0
    assert np.isnan(std)  # 单个值标准差未定义

def test_calculate_statistics_negative():
    """测试负数数据"""
    data = [-5, -4, -3, -2, -1]
    mean, std = calculate_statistics(data)

    assert np.isclose(mean, -3.0)
    assert std > 0  # 标准差总是正数
```

**测试审查要点：**
- [ ] 有单元测试覆盖
- [ ] 测试正常情况
- [ ] 测试边界情况
- [ ] 测试异常情况
- [ ] 测试命名清晰

#### 集成测试

```python
import pytest
import pandas as pd
from pathlib import Path

@pytest.fixture
def sample_data():
    """创建测试数据"""
    return pd.DataFrame({
        'subject_id': range(1, 11),
        'treatment': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'],
        'response': [23, 25, 27, 29, 31, 18, 20, 22, 24, 26]
    })

def test_full_analysis_pipeline(sample_data, tmp_path):
    """测试完整的分析流程"""
    # 保存测试数据
    data_file = tmp_path / "test_data.csv"
    sample_data.to_csv(data_file, index=False)

    # 运行分析
    from src.pipeline import run_analysis
    results = run_analysis(data_file, output_dir=tmp_path)

    # 验证输出
    assert results['p_value'] < 0.05  # 应该有显著差异
    assert (tmp_path / "results.csv").exists()
    assert (tmp_path / "figures" / "plot.png").exists()
```

**审查要点：**
- [ ] 测试完整工作流
- [ ] 使用临时目录
- [ ] 清理测试文件
- [ ] 验证输出文件

### 第七阶段：安全性和数据完整性审查

#### 数据验证

```python
import pandas as pd
import hashlib

def validate_input_data(df, schema):
    """验证输入数据的完整性和格式"""
    errors = []

    # 检查必需列
    required_columns = schema['required_columns']
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        errors.append(f"缺失必需列: {missing_cols}")

    # 检查数据类型
    for col, expected_type in schema['types'].items():
        if col in df.columns:
            if not df[col].dtype == expected_type:
                errors.append(f"列 '{col}' 类型错误: 期望 {expected_type}, 实际 {df[col].dtype}")

    # 检查值范围
    for col, (min_val, max_val) in schema.get('ranges', {}).items():
        if col in df.columns:
            if df[col].min() < min_val or df[col].max() > max_val:
                errors.append(f"列 '{col}' 值超出范围 [{min_val}, {max_val}]")

    return errors

# 使用示例
schema = {
    'required_columns': ['subject_id', 'age', 'treatment'],
    'types': {'subject_id': 'int64', 'age': 'int64', 'treatment': 'object'},
    'ranges': {'age': (0, 120)}
}

df = pd.read_csv('data.csv')
errors = validate_input_data(df, schema)
if errors:
    print("数据验证失败:")
    for error in errors:
        print(f"  - {error}")
    raise ValueError("数据验证失败")
```

#### 数据完整性检查

```python
def calculate_checksum(file_path):
    """计算文件的MD5校验和"""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest()

# 保存数据时记录校验和
data.to_csv('data.csv', index=False)
checksum = calculate_checksum('data.csv')
with open('data.csv.md5', 'w') as f:
    f.write(checksum)

# 读取数据时验证校验和
def load_data_with_verification(data_file):
    """加载数据并验证完整性"""
    checksum_file = f"{data_file}.md5"

    if os.path.exists(checksum_file):
        with open(checksum_file, 'r') as f:
            expected_checksum = f.read().strip()

        actual_checksum = calculate_checksum(data_file)

        if actual_checksum != expected_checksum:
            raise ValueError(f"数据文件校验失败: {data_file}")

        print(f"数据完整性验证通过: {data_file}")

    return pd.read_csv(data_file)
```

**审查要点：**
- [ ] 输入数据验证
- [ ] 数据完整性检查
- [ ] 敏感数据保护
- [ ] 无硬编码密码或密钥
- [ ] 日志记录适当

### 第八阶段：性能审查

#### 向量化操作

```python
import numpy as np
import time

# ❌ BAD - 循环计算（慢）
def calculate_distances_loop(points):
    n = len(points)
    distances = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distances[i, j] = np.sqrt(np.sum((points[i] - points[j])**2))
    return distances

# ✅ GOOD - 向量化计算（快）
def calculate_distances_vectorized(points):
    # 使用广播计算所有点对之间的距离
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    distances = np.sqrt(np.sum(diff**2, axis=2))
    return distances

# 性能比较
points = np.random.rand(100, 3)

start = time.time()
dist1 = calculate_distances_loop(points)
time1 = time.time() - start

start = time.time()
dist2 = calculate_distances_vectorized(points)
time2 = time.time() - start

print(f"循环方法: {time1:.4f}s")
print(f"向量化方法: {time2:.4f}s")
print(f"加速比: {time1/time2:.1f}x")
```

**审查要点：**
- [ ] 使用向量化操作（NumPy/Pandas）
- [ ] 避免不必要的循环
- [ ] 大数据集使用批处理
- [ ] 内存使用合理

## 代码审查检查清单

### 📋 完整审查清单

#### 项目组织 (5分)
- [ ] 项目结构清晰合理
- [ ] README文件完整（目的、安装、使用）
- [ ] 依赖管理（requirements.txt/environment.yml）
- [ ] 数据和代码分离
- [ ] 适当的.gitignore

#### 代码质量 (10分)
- [ ] 命名规范（变量、函数、类）
- [ ] 函数长度合理（< 50行）
- [ ] 单一职责原则
- [ ] DRY原则（无重复代码）
- [ ] 文档字符串完整
- [ ] 注释解释"为什么"
- [ ] 代码格式一致（PEP 8）
- [ ] 无注释掉的代码
- [ ] 无调试print语句
- [ ] 无硬编码的魔法数字

#### 正确性 (15分)
- [ ] 数值计算正确
- [ ] 统计方法适当
- [ ] 假设检验已执行
- [ ] 数据处理正确
- [ ] 边界情况处理
- [ ] 异常处理适当
- [ ] 数据类型正确
- [ ] 索引和切片正确
- [ ] 浮点数比较使用容差
- [ ] 缺失值处理明确

#### 可重复性 (10分)
- [ ] 随机种子固定
- [ ] 依赖版本锁定
- [ ] 路径使用相对路径
- [ ] 数据来源可追溯
- [ ] 环境可重建
- [ ] 中间结果可保存
- [ ] 参数可配置
- [ ] 无硬编码路径

#### 测试 (10分)
- [ ] 有单元测试
- [ ] 测试覆盖主要函数
- [ ] 测试边界情况
- [ ] 测试异常处理
- [ ] 集成测试存在
- [ ] 测试可运行
- [ ] 测试命名清晰

#### 文档 (5分)
- [ ] README完整
- [ ] 函数文档字符串
- [ ] 使用示例
- [ ] 安装说明
- [ ] 依赖说明

#### 安全性 (5分)
- [ ] 输入验证
- [ ] 数据完整性检查
- [ ] 无硬编码密码
- [ ] 敏感数据保护
- [ ] 日志记录适当

**总分：60分**
- 优秀：≥ 50分
- 良好：40-49分
- 合格：30-39分
- 需改进：< 30分

## 自动化代码审查工具

### Python代码质量工具

```bash
# 安装工具
pip install flake8 pylint black mypy pytest pytest-cov

# 1. Flake8 - 代码风格检查
flake8 src/ --max-line-length=100 --ignore=E203,W503

# 2. Black - 代码格式化
black src/ --line-length=100

# 3. Pylint - 代码质量检查
pylint src/ --disable=C0111,R0903

# 4. MyPy - 类型检查
mypy src/ --ignore-missing-imports

# 5. Pytest - 运行测试
pytest tests/ -v --cov=src --cov-report=html

# 6. 生成覆盖率报告
coverage report -m
```

### 配置文件示例

```ini
# setup.cfg 或 .flake8
[flake8]
max-line-length = 100
ignore = E203, W503
exclude = .git,__pycache__,docs,build,dist

[pylint]
disable = C0111, R0903
max-line-length = 100

[mypy]
ignore_missing_imports = True
```

### R代码质量工具

```r
# 安装工具
install.packages(c("lintr", "styler", "goodpractice"))

# 1. lintr - 代码风格检查
library(lintr)
lint("analysis.R")
lint_dir("R/")

# 2. styler - 代码格式化
library(styler)
style_file("analysis.R")
style_dir("R/")

# 3. goodpractice - 最佳实践检查
library(goodpractice)
gp(".")
```

## 审查报告模板

```markdown
# 代码审查报告

## 基本信息
- **审查日期**: 2026-04-06
- **审查人**: [姓名]
- **代码版本**: [Git commit hash]
- **审查范围**: [文件列表]

## 审查总结
- **总体评分**: 45/60 (良好)
- **主要发现**: 3个关键问题，5个次要问题，10个建议

## 详细发现

### 🔴 关键问题 (必须修复)

#### 1. 随机种子未固定
**位置**: `src/analysis.py:45`
**问题**: 模型训练未设置随机种子，导致结果不可重复
**建议**:
```python
import numpy as np
np.random.seed(42)
```

#### 2. 缺失值处理不当
**位置**: `src/preprocessing.py:78`
**问题**: 直接删除缺失值without记录
**建议**: 记录缺失值数量并说明处理策略

### 🟡 次要问题 (建议修复)

#### 1. 函数过长
**位置**: `src/analysis.py:100-250`
**问题**: `run_analysis()` 函数超过150行
**建议**: 拆分为多个子函数

### 💡 改进建议

#### 1. 添加类型提示
**位置**: 所有函数
**建议**: 使用类型提示提高代码可读性

## 检查清单得分

| 类别 | 得分 | 满分 |
|------|------|------|
| 项目组织 | 4 | 5 |
| 代码质量 | 7 | 10 |
| 正确性 | 12 | 15 |
| 可重复性 | 7 | 10 |
| 测试 | 6 | 10 |
| 文档 | 4 | 5 |
| 安全性 | 5 | 5 |
| **总计** | **45** | **60** |

## 后续行动

1. [ ] 修复所有关键问题
2. [ ] 修复次要问题
3. [ ] 考虑改进建议
4. [ ] 重新审查

## 审查人签名
[姓名], [日期]
```

## 常见问题与解决方案

### Q1: 如何审查别人的代码？
**A**:
1. 先理解代码目的和背景
2. 运行代码并查看输出
3. 按检查清单逐项检查
4. 提供建设性反馈
5. 区分"必须修复"和"建议改进"

### Q2: 如何接受代码审查反馈？
**A**:
1. 感谢审查人的时间和意见
2. 不要防御性回应
3. 澄清不清楚的反馈
4. 区分技术问题和风格偏好
5. 修复后更新代码

### Q3: 科研代码是否需要像生产代码一样严格？
**A**:
- 发表论文的代码：是！可重复性至关重要
- 探索性分析：可以宽松，但要记录
- 共享给他人的代码：是！
- 个人使用的代码：至少满足基本标准

### Q4: 如何平衡代码质量和研究进度？
**A**:
- 从一开始就养成好习惯
- 使用自动化工具（flake8, black）
- 设定最低标准（测试、文档、可重复性）
- 在关键节点进行审查（论文提交前、代码分享前）

## 参考资源

- [Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
- [Ten Simple Rules for Reproducible Computational Research](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285)
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [The Tidyverse Style Guide (R)](https://style.tidyverse.org/)
- [Code Review Guidelines](https://google.github.io/eng-practices/review/)
