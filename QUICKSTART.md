# Quick Start Guide

Get started with Claude Skills in minutes!

## What are Claude Skills?

Claude Skills are like instruction manuals that teach Claude to be an expert in specific tasks. Each skill contains specialized knowledge, workflows, and best practices.

## 5-Minute Quick Start

### Step 1: Choose a Skill

Browse the [Skills Catalog](SKILLS_CATALOG.md) to find a skill that matches your needs.

**Popular choices:**
- 📝 **paper**: Write academic papers
- 📊 **scientific-plotting**: Create research plots
- 🎨 **frontend-design**: Build beautiful web interfaces
- 📄 **docx**: Work with Word documents
- 🧪 **mcp-builder**: Create MCP servers

### Step 2: Open the Skill

Navigate to the skill's directory and open the `SKILL.md` file.

Example: [`skills/paper/SKILL.md`](skills/paper/SKILL.md)

### Step 3: Use the Skill

Copy the entire `SKILL.md` content and include it in your conversation with Claude:

```
I need help with [your task]. Please use this skill:

[Paste SKILL.md content here]

My specific request: [describe what you need]
```

### Step 4: Follow the Workflow

The skill will guide you through the process with:
- ✅ Step-by-step workflows
- 💡 Examples and templates  
- 🛠️ Tool recommendations
- ⚠️ Best practices and tips

## Examples

### Example 1: Write an Academic Paper

```
I need to write a research paper about neural networks.

[Paste skills/paper/SKILL.md content]

My research is about: "Efficient Transformer Architectures for NLP"
Target conference: NeurIPS 2024
```

### Example 2: Create Scientific Plots

```
I have experimental data and need to create publication-quality plots.

[Paste scientific-plotting/SKILL.md content]

My data: [describe your data]
Target journal: IEEE format
```

### Example 3: Build a Web Interface

```
I want to create a landing page for my product.

[Paste skills/frontend-design/SKILL.md content]

Product: AI-powered task manager
Style: Modern, minimalist
```

## Tips for Success

### 💡 Tip 1: Be Specific
Provide clear context and requirements when using skills.

**Good**: "Create a bar chart comparing 5 models with error bars, IEEE format"
**Better**: "Create a bar chart with error bars comparing accuracy of 5 models: Model A (0.85±0.03), Model B (0.82±0.04), Model C (0.88±0.02), Model D (0.79±0.05), Model E (0.86±0.03). IEEE double-column format (7.16 inches wide)."

### 💡 Tip 2: Combine Skills
You can use multiple skills together for complex tasks.

Example: Use `paper` + `scientific-plotting` + `graphical-abstract` for complete research paper workflow.

### 💡 Tip 3: Iterate
Skills work best with iteration. Start with the workflow, review outputs, and refine.

### 💡 Tip 4: Customize
Feel free to modify skills to match your specific needs. Skills are templates, not rigid rules.

## Common Workflows

### Academic Research Workflow
1. **Write paper**: Use `skills/paper/SKILL.md`
2. **Create plots**: Use `scientific-plotting/SKILL.md`
3. **Design TOC figure**: Use `graphical-abstract/SKILL.md`

### Web Development Workflow
1. **Design interface**: Use `skills/frontend-design/SKILL.md`
2. **Build components**: Use `skills/web-artifacts-builder/SKILL.md`
3. **Test application**: Use `skills/webapp-testing/SKILL.md`

### Document Creation Workflow
1. **Draft content**: Use `skills/doc-coauthoring/SKILL.md`
2. **Create Word doc**: Use `skills/docx/SKILL.md`
3. **Generate PDF**: Use `skills/pdf/SKILL.md`

### MCP Development Workflow
1. **Design server**: Use `skills/mcp-builder/SKILL.md`
2. **Build interface**: Use `skills/web-artifacts-builder/SKILL.md`
3. **Test integration**: Use `skills/webapp-testing/SKILL.md`

## Troubleshooting

### Problem: Skill output doesn't match my needs
**Solution**: Provide more specific requirements and examples of what you want.

### Problem: Skill is too verbose
**Solution**: Ask Claude to "summarize" or "be more concise" based on the skill.

### Problem: Need to modify a skill
**Solution**: Copy the skill, modify it locally, and use your customized version.

### Problem: Combining multiple skills
**Solution**: Reference multiple skills sequentially: "First use skill A for X, then use skill B for Y"

## Next Steps

1. 📚 **Explore**: Browse the [Skills Catalog](SKILLS_CATALOG.md) to see all available skills
2. 🎯 **Practice**: Try a skill with a real task
3. 🛠️ **Customize**: Adapt skills to your workflow
4. 🤝 **Contribute**: Create and share your own skills ([Contributing Guide](CONTRIBUTING.md))

## Resources

- [Full Documentation](README.md) - Complete repository overview
- [Skills Catalog](SKILLS_CATALOG.md) - Detailed skill reference
- [Contributing Guide](CONTRIBUTING.md) - Create your own skills
- [License Information](LICENSE.md) - Licensing details

## Support

- 🐛 **Issues**: Report bugs or request features
- 💬 **Discussions**: Ask questions and share ideas
- ⭐ **Star**: Star the repo if you find it useful!

---

Ready to get started? Pick a skill from the [catalog](SKILLS_CATALOG.md) and dive in! 🚀
