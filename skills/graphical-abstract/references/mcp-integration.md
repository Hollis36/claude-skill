# MCP工具集成指南

## 目录

1. [Figma MCP](#figma-mcp)
2. [Banana Pro MCP](#banana-pro-mcp)
3. [其他可用MCP](#其他可用mcp)

---

## Figma MCP

### 检测可用性

在使用前，先确认Figma MCP服务是否可用：

```
检查可用的MCP工具列表，查找figma相关工具
```

### 常用操作

#### 创建新文件

```javascript
// MCP调用格式
figma_create_document({
  name: "Graphical Abstract - Paper Title",
  width: 1800,
  height: 1200
})
```

#### 创建形状

```javascript
// 矩形/圆角矩形
figma_create_rectangle({
  x: 100,
  y: 200,
  width: 300,
  height: 150,
  fill: "#4A90D9",
  cornerRadius: 12,
  shadow: true
})

// 圆形
figma_create_ellipse({
  centerX: 400,
  centerY: 300,
  radiusX: 75,
  radiusY: 75,
  fill: "#E74C3C"
})

// 箭头/线条
figma_create_line({
  startX: 420,
  startY: 275,
  endX: 520,
  endY: 275,
  strokeWidth: 3,
  strokeColor: "#333333",
  arrowEnd: true
})
```

#### 添加文本

```javascript
figma_create_text({
  x: 250,
  y: 275,
  text: "Input Data",
  fontSize: 24,
  fontWeight: "bold",
  fontFamily: "Inter",
  fill: "#FFFFFF",
  textAlign: "center"
})
```

#### 分组和对齐

```javascript
// 选择多个元素并分组
figma_group({
  elements: ["rect_1", "text_1"],
  name: "Step 1"
})

// 对齐
figma_align({
  elements: ["group_1", "group_2", "group_3"],
  alignment: "center-vertical",
  distribute: "horizontal"
})
```

#### 导出

```javascript
figma_export({
  format: "png",    // png, pdf, svg, jpg
  scale: 2,         // 2x for 300 DPI
  selection: "all"  // or specific frame/group name
})
```

### 完整工作流示例

```javascript
// 1. 创建文档
const doc = figma_create_document({
  name: "GA - Neural Network Architecture",
  width: 1800,
  height: 1200
})

// 2. 创建背景
figma_create_rectangle({
  x: 0, y: 0,
  width: 1800, height: 1200,
  fill: "#FFFFFF"
})

// 3. 创建步骤框
const steps = [
  { label: "Input", color: "#667eea", x: 150 },
  { label: "Encoder", color: "#f093fb", x: 550 },
  { label: "Decoder", color: "#4facfe", x: 950 },
  { label: "Output", color: "#38ef7d", x: 1350 }
]

steps.forEach(step => {
  figma_create_rectangle({
    x: step.x, y: 450,
    width: 280, height: 150,
    fill: step.color,
    cornerRadius: 16,
    shadow: true
  })
  figma_create_text({
    x: step.x + 140, y: 525,
    text: step.label,
    fontSize: 28,
    fontWeight: "bold",
    fill: "#FFFFFF",
    textAlign: "center"
  })
})

// 4. 添加箭头
[450, 850, 1250].forEach(x => {
  figma_create_line({
    startX: x, startY: 525,
    endX: x + 80, endY: 525,
    strokeWidth: 4,
    strokeColor: "#555555",
    arrowEnd: true
  })
})

// 5. 导出
figma_export({ format: "png", scale: 2 })
```

---

## Banana Pro MCP

Banana Pro提供AI图像生成能力，适合创建：
- 装饰性背景
- 图标和符号
- 风格化元素

### 检测可用性

```
检查可用的MCP工具列表，查找banana相关工具
```

### 生成背景

```javascript
banana_generate({
  prompt: "abstract scientific background, soft blue gradient, \
           subtle molecular structures, minimalist, clean, \
           professional academic style",
  width: 1800,
  height: 1200,
  style: "photorealistic",
  negative_prompt: "text, watermark, signature, busy, cluttered"
})
```

### 生成图标

```javascript
// 神经网络图标
banana_generate({
  prompt: "flat icon of neural network brain, \
           simple geometric nodes connected by lines, \
           blue color scheme, white background, \
           minimalist vector style",
  width: 256,
  height: 256,
  style: "illustration"
})

// DNA图标
banana_generate({
  prompt: "simple DNA double helix icon, \
           clean scientific illustration, \
           green and blue colors, white background",
  width: 256,
  height: 256,
  style: "illustration"
})

// 数据流图标
banana_generate({
  prompt: "data flow icon with arrows, \
           abstract geometric shapes, \
           gradient purple to blue, \
           flat design, white background",
  width: 256,
  height: 256
})
```

### 生成示意图元素

```javascript
// 实验设备示意
banana_generate({
  prompt: "scientific laboratory equipment illustration, \
           microscope and test tubes, \
           clean vector style, isometric view, \
           soft colors, white background",
  width: 400,
  height: 400,
  style: "illustration"
})

// 计算机/服务器
banana_generate({
  prompt: "modern computer server rack illustration, \
           clean technical drawing style, \
           blue LED lights, isometric view",
  width: 400,
  height: 400
})
```

### 风格化处理

```javascript
// 将现有图像风格化
banana_img2img({
  input_image: "path/to/diagram.png",
  prompt: "professional scientific illustration style, \
           clean lines, soft shadows, academic publication quality",
  strength: 0.4  // 保留原图结构
})
```

### Prompt技巧

**学术风格关键词：**
- `scientific illustration`
- `academic publication style`
- `clean minimalist design`
- `professional technical diagram`
- `vector style`
- `flat design`
- `isometric view`

**避免使用：**
- `realistic photo`
- `complex detailed`
- `artistic creative`
- `fantasy style`

---

## 其他可用MCP

### drawsvg MCP

如果可用，可直接生成SVG代码：

```javascript
drawsvg_create({
  width: 1800,
  height: 1200,
  elements: [
    {
      type: "rect",
      x: 100, y: 400,
      width: 300, height: 200,
      fill: "#4A90D9",
      rx: 12
    },
    {
      type: "text",
      x: 250, y: 510,
      content: "Input",
      fontSize: 28,
      fill: "white",
      anchor: "middle"
    }
  ]
})
```

### Playwright MCP

用于将HTML渲染为图像：

```javascript
playwright_screenshot({
  url: "file:///path/to/graphical_abstract.html",
  viewport: { width: 1800, height: 1200 },
  output: "graphical_abstract.png",
  fullPage: false
})
```

---

## 工具选择决策树

```
需要创建摘要图
     │
     ├─── 需要精确设计控制？
     │         │
     │         ├── 是 ──▶ Figma MCP
     │         │
     │         └── 否 ──┬── 需要AI生成元素？
     │                  │
     │                  ├── 是 ──▶ Banana Pro MCP
     │                  │
     │                  └── 否 ──▶ Python/HTML方案
     │
     └─── 需要与LaTeX集成？
               │
               └── 是 ──▶ TikZ方案
```

## 混合使用策略

最佳实践是组合使用多种工具：

1. **背景/装饰** → Banana Pro生成
2. **主体框架** → Figma或Python绑制
3. **数据图表** → matplotlib生成后导入
4. **最终合成** → Figma组合并导出

```
Banana Pro          Python/matplotlib       Figma
    │                      │                  │
    ▼                      ▼                  ▼
背景图像.png  +  数据图表.png  +  布局设计  ──▶ 最终输出.png
```
