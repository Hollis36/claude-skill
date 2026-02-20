# Claude Skills Collection

[English](#english) | [中文](#中文)

---

## 📚 Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get started in 5 minutes
- **[Skills Catalog](SKILLS_CATALOG.md)** - Complete reference for all skills
- **[Contributing Guide](CONTRIBUTING.md)** - Create and share your own skills
- **[License Information](LICENSE.md)** - Licensing details for each skill

---

## English

### Overview

This repository contains a comprehensive collection of **Claude Skills** - modular, self-contained packages that extend Claude's capabilities with specialized knowledge, workflows, and tool integrations. Each skill acts as an "onboarding guide" that transforms Claude from a general-purpose agent into a specialized expert for specific domains or tasks.

### What are Skills?

Skills are structured prompts and workflows that provide:

1. **Specialized Workflows** - Multi-step procedures for specific domains
2. **Tool Integrations** - Instructions for working with specific file formats or APIs  
3. **Domain Expertise** - Domain-specific knowledge, schemas, and best practices
4. **Bundled Resources** - Scripts, references, and assets for complex tasks

### Repository Structure

```
cluade_skill/
├── skills/              # Main skills directory
│   ├── algorithmic-art/    # Generative art with p5.js
│   ├── brand-guidelines/   # Brand identity creation
│   ├── canvas-design/      # Interactive canvas designs
│   ├── doc-coauthoring/    # Collaborative document writing
│   ├── docx/               # Microsoft Word document handling
│   ├── frontend-design/    # Frontend UI/UX design
│   ├── internal-comms/     # Internal communications
│   ├── mcp-builder/        # MCP server development
│   ├── paper/              # Academic paper writing (English)
│   ├── pdf/                # PDF document handling
│   ├── pptx/               # PowerPoint presentations
│   ├── skill-creator/      # Guide for creating new skills
│   ├── slack-gif-creator/  # Slack GIF creation
│   ├── theme-factory/      # Color theme generation
│   ├── web-artifacts-builder/ # Web component creation
│   ├── webapp-testing/     # Web application testing
│   └── xlsx/               # Excel spreadsheet handling
├── graphical-abstract/     # Academic graphical abstract creation
├── review-paper-writing/   # Literature review / survey paper writing
├── scientific-plotting/    # Scientific data visualization
└── commands/              # Command templates
```

### Available Skills

#### Academic & Research
- **paper** - Academic paper writing assistant (AI/CS focus)
- **graphical-abstract** - Create journal-quality graphical abstracts and TOC figures
- **review-paper-writing** - Literature review and survey paper writing with MCP bio-research tools
- **scientific-plotting** - High-quality scientific plotting and data visualization

#### Design & Creative
- **algorithmic-art** - Generative art using p5.js with seeded randomness
- **canvas-design** - Interactive canvas designs and visualizations
- **frontend-design** - Frontend UI/UX design and development
- **theme-factory** - Color palette and theme generation
- **brand-guidelines** - Brand identity and visual guidelines

#### Document Creation
- **docx** - Microsoft Word document creation and editing
- **pdf** - PDF document generation and manipulation
- **pptx** - PowerPoint presentation creation
- **xlsx** - Excel spreadsheet creation and data handling

#### Development & Tools
- **mcp-builder** - MCP (Model Context Protocol) server development
- **web-artifacts-builder** - Build interactive web components
- **webapp-testing** - Web application testing workflows
- **skill-creator** - Guide for creating new skills

#### Communication
- **doc-coauthoring** - Collaborative document writing workflows
- **internal-comms** - Internal communications and announcements
- **slack-gif-creator** - Create engaging GIFs for Slack

### How to Use

1. **Browse Skills**: Navigate to the `skills/` directory or specialized skill folders
2. **Read Documentation**: Each skill has a `SKILL.md` file with detailed instructions
3. **Copy & Use**: Copy the skill content and provide it to Claude as context
4. **Customize**: Adapt the skills to your specific needs

### Skill Structure

Each skill typically contains:

```
skill-name/
├── SKILL.md          # Main skill definition (required)
├── LICENSE.txt       # License information
├── references/       # Additional reference materials
└── [other resources] # Scripts, templates, examples
```

### Contributing

Contributions are welcome! When creating new skills:

1. Follow the structure defined in `skills/skill-creator/SKILL.md`
2. Keep skills concise and focused
3. Include clear examples and workflows
4. Add appropriate license information

### License

Individual skills may have different licenses. Check the `LICENSE.txt` file in each skill directory for specific terms.

---

## 中文

### 概述

这个仓库包含了一个全面的 **Claude 技能集合** - 模块化的、自包含的包，通过专业知识、工作流程和工具集成来扩展 Claude 的能力。每个技能都充当"入职指南"，将 Claude 从通用助手转变为特定领域或任务的专业专家。

### 什么是技能？

技能是结构化的提示词和工作流程，提供：

1. **专业工作流程** - 特定领域的多步骤流程
2. **工具集成** - 使用特定文件格式或 API 的说明
3. **领域专业知识** - 领域特定的知识、模式和最佳实践
4. **捆绑资源** - 用于复杂任务的脚本、参考资料和资产

### 仓库结构

```
cluade_skill/
├── skills/              # 主技能目录
│   ├── algorithmic-art/    # p5.js 生成式艺术
│   ├── brand-guidelines/   # 品牌标识创建
│   ├── canvas-design/      # 交互式画布设计
│   ├── doc-coauthoring/    # 协作文档写作
│   ├── docx/               # Word 文档处理
│   ├── frontend-design/    # 前端 UI/UX 设计
│   ├── internal-comms/     # 内部沟通
│   ├── mcp-builder/        # MCP 服务器开发
│   ├── paper/              # 学术论文写作（英文）
│   ├── pdf/                # PDF 文档处理
│   ├── pptx/               # PowerPoint 演示文稿
│   ├── skill-creator/      # 创建新技能指南
│   ├── slack-gif-creator/  # Slack GIF 创建
│   ├── theme-factory/      # 配色主题生成
│   ├── web-artifacts-builder/ # Web 组件创建
│   ├── webapp-testing/     # Web 应用测试
│   └── xlsx/               # Excel 表格处理
├── graphical-abstract/     # 学术摘要图创建
├── review-paper-writing/   # 综述论文写作
├── scientific-plotting/    # 科研数据可视化
└── commands/              # 命令模板
```

### 可用技能

#### 学术与研究
- **paper** - 学术论文写作助手（AI/计算机科学方向）
- **graphical-abstract** - 创建期刊级别的图形摘要和 TOC 图
- **review-paper-writing** - 综述论文写作，集成 MCP 生物医学文献检索工具
- **scientific-plotting** - 高质量科研绘图和数据可视化

#### 设计与创意
- **algorithmic-art** - 使用 p5.js 的生成式艺术
- **canvas-design** - 交互式画布设计和可视化
- **frontend-design** - 前端 UI/UX 设计开发
- **theme-factory** - 配色方案和主题生成
- **brand-guidelines** - 品牌标识和视觉指南

#### 文档创建
- **docx** - Word 文档创建和编辑
- **pdf** - PDF 文档生成和处理
- **pptx** - PowerPoint 演示文稿创建
- **xlsx** - Excel 表格创建和数据处理

#### 开发与工具
- **mcp-builder** - MCP（模型上下文协议）服务器开发
- **web-artifacts-builder** - 构建交互式 Web 组件
- **webapp-testing** - Web 应用测试工作流
- **skill-creator** - 创建新技能指南

#### 沟通交流
- **doc-coauthoring** - 协作文档写作流程
- **internal-comms** - 内部沟通和公告
- **slack-gif-creator** - 为 Slack 创建有趣的 GIF

### 如何使用

1. **浏览技能**：导航到 `skills/` 目录或专业技能文件夹
2. **阅读文档**：每个技能都有包含详细说明的 `SKILL.md` 文件
3. **复制使用**：复制技能内容并作为上下文提供给 Claude
4. **自定义**：根据您的具体需求调整技能

### 技能结构

每个技能通常包含：

```
skill-name/
├── SKILL.md          # 主技能定义（必需）
├── LICENSE.txt       # 许可证信息
├── references/       # 额外的参考资料
└── [其他资源]        # 脚本、模板、示例
```

### 贡献

欢迎贡献！创建新技能时：

1. 遵循 `skills/skill-creator/SKILL.md` 中定义的结构
2. 保持技能简洁和专注
3. 包含清晰的示例和工作流程
4. 添加适当的许可证信息

### 许可证

各个技能可能有不同的许可证。请查看每个技能目录中的 `LICENSE.txt` 文件了解具体条款。

---

**Star this repository if you find it useful!** ⭐

如果觉得有用，请给这个仓库点个星！⭐
