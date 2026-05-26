# Examples

This directory contains practical examples and use cases for Claude Skills.

## Quick Examples

### Example 1: Academic Paper Writing
Using the `skills/paper` skill to write a research paper.

**Scenario**: You're writing a paper about "Efficient Attention Mechanisms in Transformers"

**Steps**:
1. Copy the content from `skills/paper/SKILL.md`
2. Provide it to Claude with your research context:

```
I need to write a research paper about efficient attention mechanisms.

[Paste skills/paper/SKILL.md content here]

My research focuses on:
- Reducing computational complexity of self-attention from O(n²) to O(n log n)
- Experimental results on language modeling benchmarks
- Target venue: NeurIPS 2024
```

**Expected Output**: Claude will guide you through the paper structure, help with abstract, introduction, methodology, etc.

---

### Example 2: Scientific Plotting
Using `scientific-plotting` to create publication-quality figures.

**Scenario**: You have experimental data comparing 5 models

**Steps**:
1. Copy content from `scientific-plotting/SKILL.md`
2. Provide your data:

```
I have accuracy data for 5 models and need a bar chart for my paper.

[Paste scientific-plotting/SKILL.md content]

Data:
- Model A: 0.85 ± 0.03
- Model B: 0.82 ± 0.04
- Model C: 0.88 ± 0.02
- Model D: 0.79 ± 0.05
- Model E: 0.86 ± 0.03

Format: IEEE double-column (3.5 inches wide)
```

**Expected Output**: Python code for a publication-quality bar chart with error bars.

---

### Example 3: Document Creation
Using `skills/docx` to create a formatted report.

**Scenario**: Creating a project status report

**Steps**:
1. Copy content from `skills/docx/SKILL.md`
2. Describe your report needs:

```
Create a project status report in DOCX format.

[Paste skills/docx/SKILL.md content]

Report should include:
- Executive summary
- Project milestones (3 completed, 2 in progress)
- Budget status
- Team updates
- Professional formatting with headers and sections
```

**Expected Output**: Python code using python-docx to generate the report.

---

### Example 4: MCP Server Development
Using `skills/mcp-builder` to create an MCP server.

**Scenario**: Building an MCP server for a weather API

**Steps**:
1. Copy content from `skills/mcp-builder/SKILL.md`
2. Describe your server:

```
I want to build an MCP server that connects to OpenWeatherMap API.

[Paste skills/mcp-builder/SKILL.md content]

Requirements:
- Get current weather by city name
- Get 5-day forecast
- Handle API key configuration
- Using Python with FastMCP
```

**Expected Output**: Complete MCP server implementation with proper structure.

---

### Example 5: Web Component
Using `skills/web-artifacts-builder` for interactive components.

**Scenario**: Building a task tracker interface

**Steps**:
1. Copy content from `skills/web-artifacts-builder/SKILL.md`
2. Describe your component:

```
Create an interactive task tracker as a web artifact.

[Paste skills/web-artifacts-builder/SKILL.md content]

Features:
- Add/edit/delete tasks
- Mark as complete
- Filter by status
- Modern, clean design with Tailwind CSS
```

**Expected Output**: Complete HTML artifact with React components.

---

## Complex Workflows

### Workflow 1: Complete Research Paper
Combine multiple skills for a full research workflow.

**Skills Used**: `paper` → `scientific-plotting` → `graphical-abstract`

1. **Write paper** using `skills/paper/SKILL.md`
2. **Create figures** using `scientific-plotting/SKILL.md`
3. **Design TOC graphic** using `graphical-abstract/SKILL.md`

### Workflow 2: Web Application Development
Full-stack web application development workflow.

**Skills Used**: `frontend-design` → `web-artifacts-builder` → `webapp-testing`

1. **Design UI** using `skills/frontend-design/SKILL.md`
2. **Build components** using `skills/web-artifacts-builder/SKILL.md`
3. **Test app** using `skills/webapp-testing/SKILL.md`

### Workflow 3: Business Documentation
Create comprehensive business documentation.

**Skills Used**: `doc-coauthoring` → `docx` → `pptx`

1. **Draft content** using `skills/doc-coauthoring/SKILL.md`
2. **Create Word doc** using `skills/docx/SKILL.md`
3. **Make presentation** using `skills/pptx/SKILL.md`

---

## Tips for Success

### 1. Be Specific
❌ Bad: "Make a chart"
✅ Good: "Create a bar chart with error bars, IEEE format, 3.5 inches wide"

### 2. Provide Context
Include all relevant information upfront:
- Target audience
- Format requirements
- Data or content
- Specific constraints

### 3. Iterate
Skills work best with iteration:
1. Start with the basic workflow
2. Review the output
3. Refine with specific feedback
4. Iterate until satisfied

### 4. Combine Skills
Don't hesitate to use multiple skills together for complex tasks.

---

## Real-World Use Cases

### Academia
- Writing research papers
- Creating publication figures
- Designing graphical abstracts
- Literature reviews

### Business
- Creating reports and presentations
- Internal communications
- Data analysis and visualization
- Process documentation

### Development
- Building MCP servers
- Creating web components
- Testing web applications
- API integrations

### Design
- Brand guidelines
- Color themes
- UI/UX design
- Generative art

---

## Need Help?

- Check the [Quick Start Guide](../QUICKSTART.md)
- Browse the [Skills Catalog](../SKILLS_CATALOG.md)
- Read the [Contributing Guide](../CONTRIBUTING.md) to create custom skills
- Open an issue if you encounter problems

---

**More examples coming soon!** Contributions of example use cases are welcome.
