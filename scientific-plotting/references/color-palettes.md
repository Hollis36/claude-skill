# 科研绘图配色方案参考

## 目录

1. [学术通用配色](#学术通用配色)
2. [色盲友好配色](#色盲友好配色)
3. [期刊专用配色](#期刊专用配色)
4. [渐变色板](#渐变色板)
5. [配色工具](#配色工具)

---

## 学术通用配色

### 经典学术六色

```python
ACADEMIC_6 = {
    'blue': '#0077BB',
    'cyan': '#33BBEE',
    'green': '#009988',
    'orange': '#EE7733',
    'red': '#CC3311',
    'magenta': '#EE3377',
}
```

### Nature风格

```python
NATURE_COLORS = [
    '#E64B35',  # 红
    '#4DBBD5',  # 青
    '#00A087',  # 绿
    '#3C5488',  # 蓝
    '#F39B7F',  # 橙
    '#8491B4',  # 灰蓝
    '#91D1C2',  # 浅绿
    '#DC0000',  # 深红
]
```

### Science风格

```python
SCIENCE_COLORS = [
    '#3B4992',  # 深蓝
    '#EE0000',  # 红
    '#008B45',  # 绿
    '#631879',  # 紫
    '#FF7F00',  # 橙
    '#FFD700',  # 金
]
```

---

## 色盲友好配色

### Paul Tol配色方案

推荐用于所有学术出版物，确保色盲读者可辨识。

```python
# 定性配色 (Qualitative) - 最多7类
TOL_BRIGHT = ['#4477AA', '#EE6677', '#228833', '#CCBB44', '#66CCEE', '#AA3377', '#BBBBBB']

# 高对比度 (High Contrast) - 最多3类
TOL_HIGH_CONTRAST = ['#004488', '#DDAA33', '#BB5566']

# 中等对比度 - 最多6类
TOL_MEDIUM_CONTRAST = ['#6699CC', '#004488', '#EECC66', '#994455', '#997700', '#EE99AA']

# 浅色版本
TOL_LIGHT = ['#77AADD', '#EE8866', '#EEDD88', '#FFAABB', '#99DDFF', '#44BB99', '#BBCC33']
```

### IBM配色

```python
IBM_COLORBLIND = ['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000']
```

### Wong配色（推荐）

```python
WONG_COLORS = [
    '#000000',  # 黑
    '#E69F00',  # 橙
    '#56B4E9',  # 天蓝
    '#009E73',  # 蓝绿
    '#F0E442',  # 黄
    '#0072B2',  # 蓝
    '#D55E00',  # 朱红
    '#CC79A7',  # 粉紫
]
```

---

## 期刊专用配色

### IEEE/ACM风格

```python
IEEE_COLORS = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
```

### Cell风格

```python
CELL_COLORS = [
    '#1F78B4',  # 蓝
    '#E31A1C',  # 红
    '#33A02C',  # 绿
    '#FF7F00',  # 橙
    '#6A3D9A',  # 紫
    '#B15928',  # 棕
]
```

### JAMA风格

```python
JAMA_COLORS = ['#374E55', '#DF8F44', '#00A1D5', '#B24745', '#79AF97', '#6A6599', '#80796B']
```

---

## 渐变色板

### 单色渐变（Sequential）

```python
import matplotlib.pyplot as plt

# 推荐渐变
SEQUENTIAL_MAPS = {
    'viridis': plt.cm.viridis,      # 最推荐，色盲友好
    'plasma': plt.cm.plasma,
    'inferno': plt.cm.inferno,
    'magma': plt.cm.magma,
    'cividis': plt.cm.cividis,      # 色盲优化

    # 经典单色
    'Blues': plt.cm.Blues,
    'Greens': plt.cm.Greens,
    'Oranges': plt.cm.Oranges,
    'Greys': plt.cm.Greys,
}
```

### 双向渐变（Diverging）

用于表示正负、高低对比：

```python
DIVERGING_MAPS = {
    'RdBu': plt.cm.RdBu_r,          # 红蓝（推荐）
    'RdYlBu': plt.cm.RdYlBu_r,      # 红黄蓝
    'coolwarm': plt.cm.coolwarm,    # 冷暖
    'PiYG': plt.cm.PiYG,            # 粉绿
    'PRGn': plt.cm.PRGn,            # 紫绿
}
```

### 自定义渐变

```python
from matplotlib.colors import LinearSegmentedColormap

# 创建自定义渐变
def create_gradient(colors, name='custom', n=256):
    return LinearSegmentedColormap.from_list(name, colors, N=n)

# 示例：白-蓝渐变
WHITE_BLUE = create_gradient(['#FFFFFF', '#0077BB'])

# 示例：红-白-蓝
RED_WHITE_BLUE = create_gradient(['#CC3311', '#FFFFFF', '#0077BB'])
```

---

## 配色工具

### Seaborn调色板

```python
import seaborn as sns

# 获取调色板
palette = sns.color_palette("husl", 8)  # HUSL色彩空间
palette = sns.color_palette("Set2")      # 柔和色彩
palette = sns.color_palette("tab10")     # Tableau风格

# 查看调色板
sns.palplot(palette)
```

### 颜色转换

```python
import matplotlib.colors as mcolors

# HEX转RGB
rgb = mcolors.hex2color('#0077BB')  # (0.0, 0.467, 0.733)

# RGB转HEX
hex_color = mcolors.rgb2hex((0.0, 0.467, 0.733))

# 调整透明度
rgba = (*mcolors.hex2color('#0077BB'), 0.7)  # 70%不透明度
```

### 配色验证

```python
# 检查色盲友好性的工具
# 推荐使用: https://davidmathlogic.com/colorblind/
# 或 Python包: colorspacious

from colorspacious import cspace_convert

def check_colorblind(hex_colors):
    """模拟色盲视角下的颜色"""
    for color in hex_colors:
        rgb = mcolors.hex2color(color)
        # 转换到色盲模拟空间
        deuteranopia = cspace_convert(rgb, "sRGB1", "sRGB1-linear")
        print(f"{color} -> Deuteranopia simulation")
```

---

## 配色使用建议

1. **类别不超过7个时**：使用定性配色（Qualitative）
2. **连续数值**：使用渐变色板（Sequential）
3. **有中心值的数据**：使用双向渐变（Diverging）
4. **需要强调某一类**：使用灰色作为其他类的颜色

### 避免的做法

- 红绿搭配（色盲不友好）
- 使用彩虹色（Rainbow）渐变
- 过多的颜色类别（>7个）
- 低对比度的相邻颜色
