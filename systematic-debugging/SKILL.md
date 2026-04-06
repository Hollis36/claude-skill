---
name: systematic-debugging
description: |
  系统化调试助手，帮助科研人员使用结构化方法定位和修复代码问题。支持4阶段调试流程、根因追踪技术、日志和断点策略、条件等待方法、防御式编程。当用户需要：(1) 调试科研代码错误、(2) 追踪数据分析问题、(3) 定位统计计算错误、(4) 解决实验代码bug、(5) 优化代码性能时触发。关键词：debugging、调试、bug修复、错误追踪、问题定位、troubleshooting。
license: Apache-2.0
---

# 系统化调试助手

帮助科研人员使用系统化、可重复的方法定位和修复代码问题，避免随机猜测和无效尝试。

## 核心原则

### 系统化调试的黄金法则

1. **重现优先** - 不能重现的问题无法修复
2. **假设驱动** - 基于证据提出假设，而不是猜测
3. **隔离问题** - 逐步缩小问题范围
4. **验证修复** - 确保问题真正解决，而非表面消失

## 四阶段调试流程

### 阶段 1：问题重现 (Reproduce)

**目标**：可靠地触发问题

#### 步骤 1.1：记录问题症状

```markdown
## Bug报告模板

### 问题描述
简要描述问题是什么

### 预期行为
代码应该做什么

### 实际行为
代码实际做了什么

### 重现步骤
1. 运行 `python analysis.py`
2. 使用数据集 `data/experiment_001.csv`
3. 观察输出

### 环境信息
- Python版本: 3.11.0
- 操作系统: Ubuntu 22.04
- 关键依赖: numpy==1.24.0, pandas==2.0.0

### 错误消息
```
ValueError: could not convert string to float: 'NA'
  File "analysis.py", line 45, in process_data
```

### 数据样本
提供最小化的测试数据
```

#### 步骤 1.2：创建最小可重现示例 (MRE)

```python
# ❌ BAD - 完整复杂的代码
def analyze_experiment():
    # 100+ 行代码
    data = load_data()
    preprocessed = preprocess(data)
    results = complex_analysis(preprocessed)
    # 错误在某处发生...
    return results

# ✅ GOOD - 最小可重现示例
import pandas as pd

# 错误：无法将'NA'转换为浮点数
data = pd.DataFrame({
    'value': ['1.0', '2.0', 'NA', '4.0']
})

# 这行会失败
numeric_data = data['value'].astype(float)  # ValueError!
```

**创建MRE的原则：**
- 移除所有无关代码
- 使用小数据集（< 10行）
- 保持错误可重现
- 独立运行（无外部依赖）

#### 步骤 1.3：固定输入和环境

```python
import numpy as np
import random

# 固定随机种子确保可重现
np.random.seed(42)
random.seed(42)

# 使用固定的测试数据
test_data = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

# 记录环境
print(f"NumPy版本: {np.__version__}")
print(f"测试数据: {test_data}")
```

**重现检查清单：**
- [ ] 问题可在自己机器上重现
- [ ] 创建了最小可重现示例
- [ ] 固定了随机性（如有）
- [ ] 记录了环境信息
- [ ] 问题可在他人机器上重现（可选）

---

### 阶段 2：定位问题 (Locate)

**目标**：找到导致问题的具体代码行

#### 策略 2.1：二分查找法

```python
def process_data(data):
    """使用打印语句进行二分查找"""
    print("开始处理数据")  # 检查点 1

    # 步骤 1: 加载
    loaded = load_data(data)
    print(f"加载完成: {len(loaded)} 行")  # 检查点 2

    # 步骤 2: 清理
    cleaned = clean_data(loaded)
    print(f"清理完成: {len(cleaned)} 行")  # 检查点 3

    # 步骤 3: 转换
    transformed = transform_data(cleaned)
    print(f"转换完成: shape = {transformed.shape}")  # 检查点 4

    # 步骤 4: 分析
    results = analyze(transformed)
    print(f"分析完成: {results}")  # 检查点 5

    return results

# 运行并观察哪个检查点后出现问题
```

**二分法原则：**
1. 在代码中间添加检查点
2. 运行代码观察输出
3. 如果问题在检查点前：在前半部分继续二分
4. 如果问题在检查点后：在后半部分继续二分
5. 重复直到找到问题行

#### 策略 2.2：日志记录

```python
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debug.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def analyze_data(data):
    """使用日志记录详细信息"""
    logger.debug(f"开始分析, 数据形状: {data.shape}")

    try:
        # 记录输入
        logger.debug(f"输入数据样本:\n{data.head()}")

        # 计算
        mean_value = data['value'].mean()
        logger.info(f"计算均值: {mean_value}")

        # 检查异常值
        std_value = data['value'].std()
        outliers = data[abs(data['value'] - mean_value) > 3 * std_value]
        if len(outliers) > 0:
            logger.warning(f"发现 {len(outliers)} 个异常值")

        return mean_value

    except Exception as e:
        logger.error(f"分析失败: {str(e)}", exc_info=True)
        raise
```

**日志级别使用：**
- `DEBUG`: 详细的诊断信息
- `INFO`: 正常的操作信息
- `WARNING`: 警告但不影响运行
- `ERROR`: 错误导致功能失败
- `CRITICAL`: 严重错误导致程序崩溃

#### 策略 2.3：断点调试

```python
# 使用Python调试器 (pdb)
import pdb

def problematic_function(data):
    # 在此处设置断点
    pdb.set_trace()

    # 调试时可用命令:
    # n (next) - 执行下一行
    # s (step) - 进入函数
    # c (continue) - 继续执行
    # p variable - 打印变量
    # l - 显示当前代码
    # q - 退出调试器

    result = process(data)
    return result
```

**Jupyter Notebook 调试：**
```python
# 在单元格中使用
%debug  # 在异常后进入调试器

# 或使用 IPython 调试器
from IPython.core.debugger import set_trace
set_trace()  # 设置断点
```

**VS Code / PyCharm 断点：**
- 在行号左侧点击设置断点
- F5 启动调试
- F10 单步执行
- F11 进入函数
- 查看变量面板

#### 策略 2.4：数据检查

```python
import pandas as pd
import numpy as np

def inspect_data(data, name="data"):
    """全面检查数据状态"""
    print(f"\n{'='*60}")
    print(f"检查 {name}")
    print(f"{'='*60}")

    # 基本信息
    print(f"类型: {type(data)}")
    print(f"形状: {data.shape if hasattr(data, 'shape') else 'N/A'}")

    # DataFrame 特定检查
    if isinstance(data, pd.DataFrame):
        print(f"\n列: {list(data.columns)}")
        print(f"\n数据类型:\n{data.dtypes}")
        print(f"\n缺失值:\n{data.isnull().sum()}")
        print(f"\n描述性统计:\n{data.describe()}")
        print(f"\n前5行:\n{data.head()}")

    # NumPy 数组检查
    elif isinstance(data, np.ndarray):
        print(f"数据类型: {data.dtype}")
        print(f"最小值: {data.min()}")
        print(f"最大值: {data.max()}")
        print(f"均值: {data.mean()}")
        print(f"NaN数量: {np.isnan(data).sum()}")
        print(f"Inf数量: {np.isinf(data).sum()}")

    # 列表或其他
    else:
        print(f"长度: {len(data) if hasattr(data, '__len__') else 'N/A'}")
        print(f"样本: {data[:5] if hasattr(data, '__getitem__') else data}")

# 使用示例
data = pd.read_csv('data.csv')
inspect_data(data, "原始数据")

processed = preprocess(data)
inspect_data(processed, "处理后数据")
```

---

### 阶段 3：诊断根因 (Diagnose)

**目标**：理解为什么会出现问题

#### 技术 3.1：假设-验证循环

```markdown
## 根因分析模板

### 问题症状
ValueError: could not convert string to float: 'NA'

### 假设 1: 数据包含非数值字符串
**证据需求**: 检查数据中的唯一值
**验证代码**:
```python
print(data['value'].unique())
# 输出: ['1.0', '2.0', 'NA', '4.0']
```
**结论**: ✅ 确认 - 数据中确实有 'NA' 字符串

### 假设 2: 数据加载时未正确处理缺失值
**证据需求**: 检查 read_csv 的 na_values 参数
**验证代码**:
```python
# 当前代码
data = pd.read_csv('data.csv')

# 正确代码
data = pd.read_csv('data.csv', na_values=['NA', 'N/A', 'null'])
```
**结论**: ✅ 确认 - 未指定 na_values 参数

### 根本原因
数据加载时未将 'NA' 识别为缺失值，导致被当作字符串处理，
后续类型转换时失败。
```

#### 技术 3.2：差异分析

```python
# 比较工作版本和问题版本
def compare_versions(working_data, broken_data):
    """比较两个版本的差异"""
    print("差异分析:")

    # 形状差异
    if working_data.shape != broken_data.shape:
        print(f"形状不同: {working_data.shape} vs {broken_data.shape}")

    # 数据类型差异
    if not working_data.dtypes.equals(broken_data.dtypes):
        print("\n数据类型差异:")
        for col in working_data.columns:
            if working_data[col].dtype != broken_data[col].dtype:
                print(f"  {col}: {working_data[col].dtype} -> {broken_data[col].dtype}")

    # 值差异
    differences = working_data != broken_data
    if differences.any().any():
        print(f"\n发现 {differences.sum().sum()} 个不同的值")
        print("\n不同值的位置:")
        print(differences[differences.any(axis=1)])
```

#### 技术 3.3：回溯追踪

```python
import traceback

try:
    result = problematic_function()
except Exception as e:
    # 打印完整的调用栈
    print("完整错误追溯:")
    traceback.print_exc()

    # 获取追溯对象
    tb = traceback.extract_tb(e.__traceback__)

    # 分析每一层
    print("\n调用栈分析:")
    for frame in tb:
        print(f"\n文件: {frame.filename}")
        print(f"函数: {frame.name}")
        print(f"行号: {frame.lineno}")
        print(f"代码: {frame.line}")
```

#### 技术 3.4：五个为什么

```markdown
## 五个为什么分析

### 问题: 统计分析结果不正确

**为什么1**: 为什么结果不正确？
→ 因为p值异常小 (p < 1e-50)

**为什么2**: 为什么p值异常小？
→ 因为样本量被错误计算为100000而不是100

**为什么3**: 为什么样本量计算错误？
→ 因为使用了 len(data) 而不是 len(data.dropna())

**为什么4**: 为什么使用了错误的长度？
→ 因为没有考虑缺失值的影响

**为什么5**: 为什么没有考虑缺失值？
→ 因为没有在数据加载后立即检查数据质量

### 根本原因
缺乏数据质量检查步骤

### 预防措施
在分析前添加数据验证函数
```

---

### 阶段 4：修复和验证 (Fix & Verify)

**目标**：修复问题并确保不再发生

#### 步骤 4.1：最小化修改

```python
# ❌ BAD - 大规模重写
def analyze_data(data):
    # 完全重写了整个函数
    # 引入了新的潜在问题
    pass

# ✅ GOOD - 最小化修改
def analyze_data(data):
    # 原有代码保持不变
    # ...

    # 只修复具体问题
    # 之前: numeric_data = data['value'].astype(float)
    # 之后:
    numeric_data = pd.to_numeric(data['value'], errors='coerce')

    # 原有代码继续
    # ...
```

#### 步骤 4.2：添加测试用例

```python
import pytest
import pandas as pd

def test_handle_missing_values():
    """测试缺失值处理"""
    # 创建包含缺失值的测试数据
    test_data = pd.DataFrame({
        'value': ['1.0', '2.0', 'NA', '4.0', 'N/A']
    })

    # 加载并处理
    result = process_data(test_data)

    # 验证
    assert result['value'].dtype == 'float64'
    assert result['value'].isna().sum() == 2  # 应该有2个NaN

def test_edge_case_empty_data():
    """测试空数据的边界情况"""
    test_data = pd.DataFrame({'value': []})
    result = process_data(test_data)
    assert len(result) == 0

def test_edge_case_all_na():
    """测试全为缺失值的情况"""
    test_data = pd.DataFrame({'value': ['NA', 'NA', 'NA']})
    result = process_data(test_data)
    assert result['value'].isna().all()
```

#### 步骤 4.3：回归测试

```python
# 运行所有测试确保修复没有破坏其他功能
pytest tests/ -v

# 检查测试覆盖率
pytest tests/ --cov=src --cov-report=html

# 查看覆盖率报告
# open htmlcov/index.html
```

#### 步骤 4.4：防御式编程

```python
# 添加输入验证
def analyze_data(data):
    """分析数据（带防御性检查）"""

    # 验证输入
    if not isinstance(data, pd.DataFrame):
        raise TypeError(f"期望 DataFrame, 得到 {type(data)}")

    if 'value' not in data.columns:
        raise ValueError("数据必须包含 'value' 列")

    if len(data) == 0:
        raise ValueError("数据不能为空")

    # 处理缺失值
    numeric_data = pd.to_numeric(data['value'], errors='coerce')

    # 检查转换后的数据
    if numeric_data.isna().all():
        raise ValueError("所有值都无法转换为数字")

    # 继续分析
    result = numeric_data.mean()

    # 验证输出
    if not isinstance(result, (int, float)):
        raise TypeError(f"结果应为数值, 得到 {type(result)}")

    return result
```

#### 步骤 4.5：记录修复

```markdown
## 修复记录

### Bug ID: #123
**标题**: ValueError when processing data with 'NA' strings

### 根本原因
数据加载时未将 'NA' 识别为缺失值，导致类型转换失败

### 修复方案
在 `pd.read_csv()` 中添加 `na_values=['NA', 'N/A']` 参数

### 代码变更
```diff
- data = pd.read_csv('data.csv')
+ data = pd.read_csv('data.csv', na_values=['NA', 'N/A', 'null'])
```

### 测试
- [x] 添加了测试用例 `test_handle_missing_values`
- [x] 所有现有测试通过
- [x] 手工测试原始问题数据

### 防止复发
- 添加了数据验证函数
- 更新了数据加载文档
- 在代码审查检查清单中添加了此项

### 修复人: [姓名]
### 日期: 2026-04-06
```

---

## 常见问题类型和调试策略

### 类型 1: 数据相关问题

#### 问题：数据格式错误

```python
# 症状：类型转换失败
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 诊断工具
def diagnose_data_types(df):
    """诊断数据类型问题"""
    print("数据类型检查:")
    print(df.dtypes)

    print("\n每列的唯一类型:")
    for col in df.columns:
        unique_types = df[col].apply(type).unique()
        print(f"{col}: {unique_types}")

    print("\n可能的问题值:")
    for col in df.columns:
        if df[col].dtype == 'object':
            # 尝试转换为数值
            try:
                pd.to_numeric(df[col])
            except:
                problem_values = df[col][pd.to_numeric(df[col], errors='coerce').isna()]
                if len(problem_values) > 0:
                    print(f"{col}: {problem_values.unique()[:5]}")
```

#### 问题：缺失值处理

```python
# 症状：计算结果为 NaN
# result = data.mean()  # returns NaN

# 诊断
print(f"缺失值数量: {data.isna().sum()}")
print(f"缺失值比例: {data.isna().mean():.2%}")

# 修复选项
# 1. 删除缺失值
clean_data = data.dropna()

# 2. 填充缺失值
filled_data = data.fillna(data.mean())

# 3. 插值
interpolated_data = data.interpolate()
```

### 类型 2: 逻辑错误

#### 问题：循环逻辑错误

```python
# ❌ BAD - 索引错误
for i in range(len(data)):
    if data[i] > threshold:
        data[i+1] = 0  # IndexError when i = len(data)-1!

# ✅ GOOD - 正确的边界检查
for i in range(len(data) - 1):  # 注意范围
    if data[i] > threshold:
        data[i+1] = 0
```

#### 问题：条件逻辑错误

```python
# ❌ BAD - 逻辑错误
if age >= 18 and age <= 65:
    category = 'adult'
elif age >= 65:
    category = 'senior'
else:
    category = 'minor'
# 问题：65岁既满足第一个也满足第二个条件

# ✅ GOOD - 互斥条件
if age < 18:
    category = 'minor'
elif age < 65:
    category = 'adult'
else:
    category = 'senior'
```

### 类型 3: 数值计算问题

#### 问题：浮点数精度

```python
# 症状：相等比较失败
a = 0.1 + 0.2
print(a == 0.3)  # False!
print(a)  # 0.30000000000000004

# 修复：使用容差比较
import math
print(math.isclose(a, 0.3))  # True

# 或使用 numpy
import numpy as np
print(np.isclose(a, 0.3))  # True
```

#### 问题：整数除法

```python
# Python 2 风格的整数除法
result = 5 / 2  # Python 3: 2.5, Python 2: 2

# 确保浮点除法
result = 5 / 2.0
# 或
result = 5 / float(2)
# 或
from __future__ import division  # Python 2
```

### 类型 4: 性能问题

#### 问题：代码运行缓慢

```python
import time

# 性能分析
start = time.time()
result = slow_function(data)
end = time.time()
print(f"执行时间: {end - start:.2f} 秒")

# 使用 cProfile
import cProfile
cProfile.run('slow_function(data)')

# 使用 line_profiler
# pip install line_profiler
# kernprof -l -v script.py
@profile
def slow_function(data):
    # 代码
    pass
```

## 调试工具箱

### Python 调试工具

```bash
# 1. pdb - Python调试器
python -m pdb script.py

# 2. ipdb - IPython调试器
pip install ipdb
ipdb.set_trace()

# 3. pudb - 全屏调试器
pip install pudb
pudb.set_trace()

# 4. 性能分析
python -m cProfile -o output.prof script.py
python -m pstats output.prof

# 5. 内存分析
pip install memory_profiler
python -m memory_profiler script.py
```

### Jupyter Notebook 调试

```python
# 魔法命令
%pdb  # 自动进入调试器
%debug  # 在异常后进入调试器
%time statement  # 计时单个语句
%timeit statement  # 多次运行并计时
%lprun -f func func(args)  # 行级性能分析
%memit statement  # 内存使用
```

### R 调试工具

```r
# 1. 基本调试
debug(function_name)  # 启用调试
undebug(function_name)  # 禁用调试

# 2. 浏览器调试
browser()  # 在代码中设置断点

# 3. 追踪
traceback()  # 显示调用栈

# 4. 条件断点
if (x > 100) browser()

# 5. 性能分析
Rprof("output.out")
# ... 运行代码 ...
Rprof(NULL)
summaryRprof("output.out")
```

## 调试检查清单

### 🔍 开始调试前

- [ ] 保存当前工作（Git commit）
- [ ] 阅读错误消息完整内容
- [ ] 确认问题可重现
- [ ] 创建问题的最小示例
- [ ] 检查最近的代码变更

### 🔎 调试过程中

- [ ] 使用系统化方法（四阶段流程）
- [ ] 记录假设和验证结果
- [ ] 避免同时修改多处
- [ ] 每次只测试一个假设
- [ ] 保持调试日志

### ✅ 修复后

- [ ] 问题确实解决（不是表面消失）
- [ ] 添加了测试用例
- [ ] 所有测试通过
- [ ] 代码审查通过
- [ ] 记录了根本原因和修复方法

## 参考资源

- [Python Debugging With Pdb](https://realpython.com/python-debugging-pdb/)
- [Debugging in Python](https://www.youtube.com/watch?v=QU158nGABxI)
- [The Art of Debugging](https://www.amazon.com/Art-Debugging-GDB-DDD-Eclipse/dp/1593271743)
- [Systematic Debugging](https://www.cs.cornell.edu/courses/cs312/2006fa/lectures/lec26.html)
